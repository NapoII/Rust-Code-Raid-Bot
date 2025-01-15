import os
import sys
import time
import keyboard
import pyautogui
from util.__funktion__ import *
import logNow

# Predefined Variables
file_path = os.path.normpath(os.path.dirname(sys.argv[0]))
config_dir = os.path.join(file_path, "cfg", "config.ini")
config_dir = new_path(config_dir)
BSP_config = read_config(config_dir, "Test", "abc")

# Adjust the code list logic for any number of players
def get_code_list_from_file(file_path, player_num, total_players):
    """
    Generate a filtered code list for a specific player in a multi-player mode from the main file, reversed to start from top to bottom.

    :param file_path: Path to the full code list file
    :param player_num: Current player's index (1-based)
    :param total_players: Total number of players
    :return: List of codes for the player
    """
    with open(file_path, 'r') as file:
        full_code_list = [line.strip() for line in file.readlines()][::-1]  # Reverse the list
    return [code for index, code in enumerate(full_code_list) if index % total_players == (player_num - 1)]

# Main Script
# Rust-Code-Raid-Bot.py

# Setup Program Paths
file_path = os.path.dirname(os.path.abspath(__file__))
full_code_list_path = new_path(file_path, "util", "Full_Code_List_10000.txt")

# Create Main Folder
main_folder = Folder_gen("Rust - Key-Bot", "Documents")
raid_list_folder = Folder_gen("Raid-List", "Documents/Rust - Key-Bot")  # Create Raid folder

raid_list = Raid_List(raid_list_folder)
list_for_text = raid_list[0]
raid_list_text = List_to_Text(list_for_text)

# Get Raid Configuration
raid_config = Raid_cheack(raid_list, raid_list_text)
raid_name = raid_config[0]
code_start = raid_config[1]
code_end = raid_config[2]
is_new_raid = raid_config[3]
raid_folder = os.path.join(raid_list_folder, raid_name)
code_list_length = (code_end + 1) - code_start

# If new raid, create log and initialize code list
if is_new_raid:
    date_time = time.strftime("%d_%m-%Y-%H:%M")
    raid_log_path = Create_File(f"{raid_name}.txt", raid_folder, " Raid Log:\n")

    log_intro = (
        f"\nThe CodeLock Raid [{raid_name}] was created on {date_time}.\n"
        f"{code_list_length} out of 10,000 possible codes will be checked.\n"
        f"The code list starts at code number [{code_start}] and ends at [{code_end + 1}].\n\n"
        "############################################################\n\n"
        "Entered codes (use CTRL + F to search for a code):\n\n"
    )

    Fill_Text_datei(raid_log_path, log_intro, "a")

# Ask if the player is solo or with others
player_mode = pyautogui.prompt(
    text="Are you playing solo or with others? Enter '1' for solo, or the number of players (e.g., 3 for three players):",
    title="Player Mode Selection",
    default='1'
)

# Validate input
try:
    player_count = int(player_mode)
    if player_count < 1:
        raise ValueError("Player count must be at least 1.")
except ValueError as e:
    pyautogui.alert(f"Invalid input: {e}")
    sys.exit(1)

# Adjust code entry logic based on player count
if player_count == 1:
    pyautogui.alert("Solo mode selected. The bot will try all codes sequentially.")
else:
    pyautogui.alert(f"{player_count} players selected. The bot will alternate codes for each player.")

# Generate the code list for the current player
if player_count > 1:
    # Ask which player is running the bot
    player_index = pyautogui.prompt(
        text=f"Which player are you? Enter your player number (1 to {player_count}):",
        title="Player Number Selection",
        default='1'
    )
    try:
        player_index = int(player_index)
        if not (1 <= player_index <= player_count):
            raise ValueError("Player number out of range.")
    except ValueError as e:
        pyautogui.alert(f"Invalid input: {e}")
        sys.exit(1)

    # Create the filtered code list for the current player
    raid_code_list_path = Create_File(f"Code_List_Player_{player_index}.txt", raid_folder, "")
    player_code_list = get_code_list_from_file(full_code_list_path, player_index, player_count)

    # Save the filtered list to the player's file
    with open(raid_code_list_path, 'w') as file:
        for code in player_code_list:
            file.write(f"{code}\n")
else:
    # Solo mode: all codes are used
    raid_code_list_path = Create_File("Code_List.txt", raid_folder, "")
    with open(full_code_list_path, 'r') as full_file:
        with open(raid_code_list_path, 'w') as new_file:
            new_file.write(full_file.read())

# Set Hotkey
hotkey = pyautogui.prompt(
    text="Modify the HOTKEY to open the CodeLock if necessary.",
    title='HotKey Settings',
    default='alt + E'
)
print(f"The hotkey to enter the code in Rust is set to [{hotkey}].\n")

# Game Instructions
print("Switch the in-game chat to Team Chat by pressing [Enter] and then [TAB].\n")
pyautogui.alert("Switch the in-game chat to Team Chat by pressing [Enter] and then [TAB].")

print(f"Open a Code Lock in-game and press [{hotkey}] to automatically enter the code!")
pyautogui.alert(f"Open a Code Lock in-game and press [{hotkey}] to automatically enter the code!")

# Main Program
Caps_Lock_off()  # Ensure Caps Lock is turned off
start_time = time.time() + 1
attempt_count = 1

while True:
    if keyboard.is_pressed(hotkey):
        Caps_Lock_off()

        rust_window = that_window_pos("Rust")
        if not rust_window:
            continue

        try:
            pin_code = next_code(raid_code_list_path)
            Caps_Lock_off()
        except Exception:
            break

        with open(raid_code_list_path) as code_file:
            total_lines = sum(1 for _ in code_file)
            attempt_count += 1
            elapsed_time = (time.time() - start_time) / 60  # Time in minutes
            remaining_codes = code_list_length - total_lines
            completion_percentage = round((100 / code_list_length) * remaining_codes, 2)

            pins_per_minute = round(attempt_count / elapsed_time, 3)
            time_to_complete = round(((1 / pins_per_minute) * total_lines) / 60, 2)

        Caps_Lock_off()

        # Prepare and send chat message
        chat_text = (
            f">>{pin_code}<< | [{code_list_length - 1 - total_lines}/{code_list_length - 1}] Pins | "
            f"[{pins_per_minute}] Pins/min | Time until 100%: [{time_to_complete}]h | "
            f"Progress: [{completion_percentage}/100]%"
        )
        print(f"\n{chat_text}")
        Eingabe(pin_code)
        Chat(chat_text)
        Fill_Text_datei(raid_log_path, f"{chat_text}\n", "a")

        time.sleep(0.5)
    time.sleep(0.01)

print("All pins have been entered.")
pyautogui.alert("All pins have been entered.")
