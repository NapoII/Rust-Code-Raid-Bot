"""Full Doku on: https://github.com/NapoII/Rust-Code-Raid-Bot"
-----------------------------------------------
!!! ADD MUST HAVE INFO !!
------------------------------------------------
"""

# import

import os
import sys

from util.__funktion__ import *
import keyboard

# pre Var

file_path = os.path.normpath(os.path.dirname(sys.argv[0]))
config_dir = file_path + os.path.sep + "cfg" + os.path.sep + "config.ini"
config_dir = new_path(config_dir)
BSP_config = read_config(config_dir, "Test", "abc")


# Main
# Rust-Code-Raid-Bot.py

# Pre Set  Programm

file_path = os.path.dirname(os.path.abspath(__file__))
Full_Code_List_dir = new_path(file_path, "util", "Full_Code_List_10000.txt")
# Main Folder erstellen
Main_Folder = Folder_gen("Rust - Key-Bot", "Documents")
Raid_List_Folder = Folder_gen(
    "Raid-List", "Documents/Rust - Key-Bot")   # Raid Folder erstellen

Raid_List = Raid_List(Raid_List_Folder)

List_for_text = Raid_List[0]
Raid_List_Text = List_to_Text(List_for_text)

Raid_config = Raid_cheack(Raid_List, Raid_List_Text)
Raid_Name = Raid_config[0]
Code_Start = (Raid_config[1])
Code_Ende = (Raid_config[2])
Raid_New = Raid_config[3]
Raid_Folder = Raid_List_Folder + "/" + Raid_Name
Code_Listen_länge = (Code_Ende+1)-Code_Start

if Raid_New == True:
    datei_Date = Date_Time = (time.strftime("%d_%m-%Y-%H:%M"))

    Raid_log_dir = Create_File(f"{Raid_Name}.txt", Raid_Folder, " Raid_lo:\n")
    f1 = "\n Der CodeLock Raid ["+Raid_Name + "] wurde erstellt am " + str(datei_Date)+"\nEs werden "+str(Code_Listen_länge)+" von 10000 Code Möglichkeiten abgefragt./nDie Code Liste startet ab Code Nr ["+str(
        Code_Start)+" bis "+str(Code_Ende+1) + "]\n\n ############################################################\n\nEingegebene Codes (STRG + F Um nach einem Code zu suchen):\n\n"
    Fill_Text_datei(Raid_log_dir, f1, "a")
    Raid_Rest_CodeList_dir = Create_File("Code_List.txt", Raid_Folder, "")
    Code_List(Code_Start, Code_Ende, Full_Code_List_dir,
              Raid_Rest_CodeList_dir)

else:
    Raid_log_dir = new_path(Raid_Folder, f"{Raid_Name}.txt")

hotkey = pyautogui.prompt(text="Ändere bei bedraf den HOTKEY um den CodeLock zu öffnen.",
                          title='HotKey Einstellung', default='alt + E')
print(
    "Der HotKey um in Rust den Code einzugeben liegt auf ["+str(hotkey)+"]\n")

print("Stelle den In Game-Chat mit [Enter] und dann [TAB] auf Teamchat um.\n")
pyautogui.alert(
    "Stelle den In Game-Chat mit [Enter] und dann [TAB] auf Teamchat um.")
print("Öffne nun in Game einen Code Lock und Drücke [" + (
    hotkey) + "] um den Code Automatsich einzugeben!")
pyautogui.alert("Öffne nun in Game einen Code Lock und Drücke ["+str(
    hotkey)+"] um den Code Automatsich einzugeben!")

###################################

####################################################################################################
# Main Programm

Caps_Lock_off()

start_time_Z = time.time()+1

Z = 1
while True:

    if keyboard.is_pressed(hotkey):
        Caps_Lock_off()

        Rust = that_window_pos("Rust")
        if Rust == False:
            continue
        else:

            try:
                Pin = next_code(Raid_Rest_CodeList_dir)
                Caps_Lock_off()
            except:
                break

            with open(Raid_Rest_CodeList_dir) as myfile:
                total_lines = sum(1 for line in myfile)
                Z = Z + 1
                current_time_Z = time.time()
                # berechung Zeit
                elapsed_time_Z = ((current_time_Z - start_time_Z)/60)
                Restlänge = Code_Listen_länge-total_lines
                Prozent = (100/Code_Listen_länge)*Restlänge
                Prozent = round(Prozent, 2)

                Pin_pro_min = (Z/elapsed_time_Z)
                Time_for_10k = round((((1/Pin_pro_min)*total_lines))/60, 2)
                Pin_pro_min = round(Pin_pro_min, 3)
            Caps_Lock_off()
            Chat_Text = ">>" + str(Pin) + "<< | [" + str(Code_Listen_länge-1 - total_lines) + "/" + str(Code_Listen_länge-1) + "]Pins | [" + str(
                Pin_pro_min) + "]Pin/min | Zeit bis 100% : ["+str(Time_for_10k) + "]h | Fortschritt : [" + str(Prozent)+"/100]%"
            print("\n"+Chat_Text)
            Eingabe(Pin)
            # time.sleep(0.7)
            Chat(Chat_Text)
            Fill_Text_datei(Raid_log_dir, Chat_Text+"\n", "a")

        time.sleep(0.5)

        time.sleep(0.05)
    time.sleep(0.01)

print("Es wurden alle Pins Eingegeben")
pyautogui.alert("Es wurden alle Pins Eingegeben")
