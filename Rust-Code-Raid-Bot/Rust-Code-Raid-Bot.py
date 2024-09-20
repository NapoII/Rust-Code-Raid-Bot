"""
Full Documentation available at: https://github.com/NapoII/Rust-Code-Raid-Bot
------------------------------------------------------
!!! ADD NECESSARY INFORMATION HERE !!!
------------------------------------------------------
"""

# Imports
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
    
    raid_code_list_path = Create_File("Code_List.txt", raid_folder, "")
    Code_List(code_start, code_end, full_code_list_path, raid_code_list_path)
else:
    raid_log_path = new_path(raid_folder, f"{raid_name}.txt")

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
