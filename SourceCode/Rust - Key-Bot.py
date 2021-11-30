####################################################################################################
# #   Intro

v = "1.0.0"
f0 = """                   .,+%####%+,.                   
                .:#MMMMMMMMMMM@%,                 
               :@MMMMMMMMMMMMMMMM#:               
             ,#MMMMMMMMMMMMMMMMMMMM#.                                   
          +MMMMMMMMMMMMMMMMMMMMMMMMMMMM+          
         :MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM:         
        ,MMMMMMMMMMMMM@#%%#@MMMMMMMMMMMM@.        
       .@MMMMMMMMMM@+.      ,+MMMMMMMMMMM#        
       +MMMMMMMMMM%.          .%MMMMMMMMMM:       
      .@MMMMMMMMM:              +MMMMMMMMM@.      
      +MMMMMMMMM:                +MMMMMMMMM:      
      #MMMMMMMM+                  %MMMMMMMM#          
     %MMMMMMM@                     .MMMMMMMM+     
     @MMMMMMM%                      #MMMMMMM#     
     @MMMMMMM:                      +MMMMMMM#     
    .MMMMMMMM:                      :MMMMMMM@        
    .MMMMMMMM,                      :MMMMMMM@     
    .MMMMMMMM,                      :MMMMMMM@     
 .+##MMMMMMMM@######################@MMMMMMMM##:  
 %MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM% 
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM%
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM%
#MMMMMMMMMMMMMMMMMMMMM#:,,:#MMMMMMMMMMMMMMMMMMMMM%
#MMMMMMMMMMMMMMMMMMMM:      +MMMMMMMMMMMMMMMMMMMM%
#MMMMMMMMMMMMMMMMMMM:        +MMMMMMMMMMMMMMMMMMM%
#MMMMMMMMMMMMMMMMMM@         .@MMMMMMMMMMMMMMMMMM%
#MMMMMMMMMMMMMMMMMM+          %MMMMMMMMMMMMMMMMMM%
#MMMMMMMMMMMMMMMMMM:          +MMMMMMMMMMMMMMMMMM%
#MMMMMMMMMMMMMMMMMM+          %MMMMMMMMMMMMMMMMMM%
#MMMMMMMMMMMMMMMMMM#          @MMMMMMMMMMMMMMMMMM%
#MMMMMMMMMMMMMMMMMMM,        :MMMMMMMMMMMMMMMMMMM%
#MMMMMMMMMMMMMMMMMMM@       .MMMMMMMMMMMMMMMMMMMM%
#MMMMMMMMMMMMMMMMMMMM       .MMMMMMMMMMMMMMMMMMMM%
#MMMMMMMMMMMMMMMMMMMM       .MMMMMMMMMMMMMMMMMMMM%
#MMMMMMMMMMMMMMMMMMMM+      %MMMMMMMMMMMMMMMMMMMM%
#MMMMMMMMMMMMMMMMMMMMM@@@@@@MMMMMMMMMMMMMMMMMMMMM%
 %MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+ 
  :%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%,  
                                                  
 +.  :,.++++.+.   :,         ,+%+.    ,%+. .+++++:
 M. ,@.:@###.+%  .@.         +#+%@.  %@+%@.,##M##+
 M. #: :#    .@. +%          +%  #: ,@.  +#   #,  
 M.:#  :#     #: #,          +%  %+ #:   .M.  #,  
 M,@.  :#     :#,#           +% .@. @.    #,  #,  
 M%#   :@###  .@%:           +@#@+ .M     %+  #,  
 M#@,  :#:::   +@.    .::,   +#:+@,.M     %+  #,  
 M.:#  :#      :#     ,##:   +%  +% M.    %:  #,  
 M..@, :#      :#            +%  ,# #,   .@.  #,  
 M. +# :#      :#            +%  :# +#   :#   #,  
 M. .@,:@+++.  :#            +%,:@: .@%,:@,   #,  
 #.  :+,####,  ,+            :##%:   .%##,    %. 
 
            - created by Napo_II
                  - """ + v + """
               - python 3.7
- https://github.com/NapoII/Rust-Code-Raid-Bot

"""
#print(f0)
print(" \nProgramm wird gestartet ...")

####################################################################################################
# Import

#import cv2                  # für Bild erkennung
import numpy as np          # für Bild erkennung
import pyautogui            # für Bildschirm screanshot und Maus bewegung
import os                   # um Ordner des Scripts zu ermitteln
from win32gui import FindWindow, GetWindowRect
import time
import sys, os
import keyboard
import win32api,win32con

####################################################################################################

def Folder_gen(Folder_Name, Folder_dir ):
   print("Ordner Struktur wird überprüft und ggf. angelegt...\n")
   folder = Folder_Name
   dir = "~/"+str(Folder_dir)+"/"+str(folder)           # gibt gewünschten Datei-Pfad an
   full_path = os.path.expanduser(dir)                 # ergänzt datei pfad mit PC User name
   if os.path.exists(full_path):                       # Prüft datei pfad nach exsistänz Ture/False
      print("Ordner Struktur existiert bereits")
      print("  ->   " + str(full_path))
   else:                                               # Erstellt Ordner falls nicht vorhadnen
      os.makedirs(full_path)
      print("Der Ordner ["+folder+"] wurde erstellt im Verzeichnis:" )
      print("  ->   " + str(full_path))
   print("\n")
   return(full_path)

def Raid_List(Raid_Folder):     # Schaut nach Base ornder
    Raid_List = []
    
    for file in os.listdir(Raid_Folder):
            Raid_List.append(file)

    Raid_List_Len = len(Raid_List)
    if Raid_List_Len == 0 :
        print("Es wurden keine gespeicherten Code-Lock-Raids gefunden. Starten sie einen Neuen!\n")
        return False
    else:
        print ("\nEs wurden folgende gespeicherten CodeLock Raids gefunden:\n >>> "+ str(Raid_List)+"\n")
    return Raid_List

def Raid_cheack(Raid_List):
    if Raid_List == False:
        #Raid_Name = input("Wie soll dein Raid heißen: \n>>> ")
        Raid_Name = pyautogui.prompt(text='Wie soll dein Raid heißen?', title='Neuen Raid Erstellen' , default='CodeLock-Raid-1')

        #Raid_Name = Raid_Name.replace(" ", "")
        Raid_List = []
    else:
        #Raid_Name = input("Gebe gespeicherten Code Lock Raid Namen ein oder einen Namen für einen Neuen Code-Lock Raid: \n >>> " )
        Raid_Name = pyautogui.prompt(text="""Öffne einen Vorhandenen Raid oder erstelle einen neuen.
        
        Es wurden folgende gespeicherten CodeLock Raids gefunden:\n """+ str(Raid_List), title='Raid Öffnen' , default='CodeLock-Raid-1')

        
    Code_Start = int(pyautogui.prompt(text='Code Raid Start an Stelle: (1-10000)', title='Code Start Position' , default='1'))-1

    if Raid_Name in Raid_List:
        return Raid_Name, Code_Start, False
    else:
        x_Raid_Folder = Folder_gen( Raid_Name, "Documents/Rust - Key-Bot/Raid-List" )   # Main Folder erstellen
        return Raid_Name, Code_Start, True

def Erstelle_TextDatei( Text_File_name, save_path, Inhalt ):
    complete_Path_Text = os.path.join(save_path+"\\"+Text_File_name+".txt")     # Path + text datei name
    if os.path.exists(complete_Path_Text):
        return complete_Path_Text
    else:
        print("\nTextdatei ["+str(Text_File_name)+".txt] wird erstellt...")
        file1 = open(complete_Path_Text, "w")                                         # Datei erstellen
        #toFile = input("Write what you want into the field")                   # Datei input def.
        file1.write(Inhalt)                                                    # Datei wird gefüllt mit input
        file1.close()
        return complete_Path_Text

def Fill_Text_datei(Datei_dir, Fill, Atribut):
    file1 = open(Datei_dir, Atribut)                                         # Datei erstellen
    file1.write(str(Fill))                                                    # Datei wird gefüllt mit input
    file1.close()
    #print ("Die Text Datei >>> ["+ str(Datei_dir)+"] wurde beschreiben.")

def that_window_pos(window_name):

    # FindWindow takes the Window Class name (can be None if unknown), and the window's display text. 
    
    while True:
        try:
            window_handle = FindWindow(None, window_name)
            window_rect   = GetWindowRect(window_handle)
            break
        except:
            print (" Das Fenster >>> "+str(window_name)+" <<< konnte nicht gefunden werden")
            window_rect = False
            pyautogui.alert("Der HOTKEY: ["+str(hotkey)+"] Funktioniert nur im Game Rust.")
            break

    #print("Das Fenster >> "+ str(window_name) + "<<< ist auf pos > "+ str(window_rect))
    #(0, 0, 800, 600)
    return window_rect

def Zeit_pause(seconds):
    start_time = time.time()
    while True:                             # Zeit schelife startet
        current_time = time.time()
        elapsed_time = current_time - start_time        # berechung rest Zeit
        if elapsed_time > seconds:
            break

def Next_Code(Code_path):

    with open(Code_path, 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
        Next_Code = last_line 

#    Datei = open(Code_path, 'r')
#    for Next_Code in list(Datei)[::-1]:
#        break
    Next_Code = Next_Code[0:4]
    print("Aktueller Pin >>>["+str(Next_Code)+"]<<<\n")

    readFile = open(Code_path)
    lines = readFile.readlines()
    readFile.close()

    w = open(Code_path,'w')
    w.writelines([item for item in lines[:-1]])
    w.close()
    return Next_Code

def Code_List(Code_Start, Full_Code_List_dir, Raid_Rest_CodeList_dir):
    x = Code_Start
    x = 10000 - x
    y = 0
    z = x

    while True:
        x = x - 1
        y = y + 1
        if x == -1 :
            break
        with open(Full_Code_List_dir) as f:
            data = f.readlines()[x]
            print(str(int(100/int(z)*y))+" %")
        
        Fill_Text_datei(Raid_Rest_CodeList_dir, data, "a")

    print("fertig!\n")

def Caps_Lock_off():
    caps_status = 0
    caps_status = win32api.GetKeyState(win32con.VK_CAPITAL)
    if caps_status==0:
        caps_status
    else:
        Zeit_pause(0.1)
        print('CapsLock is on')
        pyautogui.press('capslock')
        Zeit_pause(0.1)

def Eingabe(Eingabe):
    Caps_Lock_off()
    Zeit_pause(0.5)
    pyautogui.write(Eingabe, interval=0.05)
    Zeit_pause(0.1)
    pyautogui.press('enter')
    Zeit_pause(0.1)

def Chat(Eingabe):
    Caps_Lock_off()
    Zeit_pause(0.5)
    pyautogui.press('enter')
    Zeit_pause(0.1)
    pyautogui.write(Eingabe, interval=0.00)
    Zeit_pause(0.1)
    pyautogui.press('enter')
    Zeit_pause(0.1)

####################################################################################################
#Pre Set  Programm

file_path = os.path.dirname(sys.argv[0])
Full_Code_List_dir = file_path + "/Work_Folder/Full Code List 10000.txt"

Main_Folder = Folder_gen( "Rust - Key-Bot","Documents" )   # Main Folder erstellen
Work_Folder = file_path + "/Work_Folder"
Raid_List_Folder = Folder_gen( "Raid-List","Documents/Rust - Key-Bot" )   # Raid Folder erstellen

print(f0)
Raid_List = Raid_List(Raid_List_Folder)

Raid_config = Raid_cheack(Raid_List)
Raid_Name = Raid_config[0]
Code_Start = (Raid_config[1])
Raid_New = Raid_config[2]
Raid_Folder = Raid_List_Folder + "/" + Raid_Name

if Raid_New == True:
    datei_Date = Date_Time=(time.strftime("%d_%m-%Y-%H:%M"))
    Raid_log_dir = Erstelle_TextDatei( Raid_Name , Raid_Folder, f0 )
    f1 = "\n Der CodeLock Raid ["+Raid_Name +"] wurde erstellt am "+ str(datei_Date)+"\nEs werden "+str(10000-Code_Start)+" von 10000 Code Möglichkeiten abgefragt./nDie Code Liste startet ab Code Nr ["+str(Code_Start)+"]\n\n ############################################################\n\nEingegebene Codes (STRG + F Um nach einem Code zu suchen):\n\n"
    Fill_Text_datei(Raid_log_dir, f1, "a")
else:
    Raid_log_dir = os.path.join(Raid_Folder+"\\"+Raid_Name+".txt")     # Path + text datei name

Raid_Rest_CodeList_dir = Erstelle_TextDatei( "Code List" , Raid_Folder,"" )



if Raid_New == True:
    Code_List(Code_Start, Full_Code_List_dir, Raid_Rest_CodeList_dir)

pyautogui.alert("Stelle den In Game-Chat mit [Enter] und dann [TAB] auf Teamchat um.")
###################################

####################################################################################################
#Main Programm
hotkey = pyautogui.prompt(text="Ändere bei bedraf den HOTKEY zum CodeLock zu öffnen.", title='HotKey Einstellung' , default='alt + E')
pyautogui.alert("Schaue gewünschten KeyLOOK an und Drücke ["+str(hotkey)+"] um den Code Automatsich einzugeben")

Caps_Lock_off()

start_time_Z = time.time()+1
Z = 1
while True:
    if keyboard.is_pressed(hotkey):
        Caps_Lock_off()
        
        Rust = that_window_pos("Rust")
        try:
            Pin = Next_Code(Raid_Rest_CodeList_dir)
            Caps_Lock_off()
        except:
            break

        with open(Raid_Rest_CodeList_dir) as myfile:
            total_lines = sum(1 for line in myfile)
            Z = Z + 1
            current_time_Z = time.time()
            elapsed_time_Z = ((current_time_Z - start_time_Z)/60)       # berechung Zeit

            Pin_pro_min = (Z/elapsed_time_Z)
            Time_for_10k = round((((1/Pin_pro_min)*total_lines))/60,2)
            Pin_pro_min = round(Pin_pro_min,3)
        Caps_Lock_off()
        Chat_Text = ">>"+Pin+"<< Noch "+str(total_lines)+" Pins. (Pin/min) : "+str(Pin_pro_min) + " Rest Zeit für Alle Pins (h) : "+str(Time_for_10k)
        print("\n"+Chat_Text)
        Eingabe(Pin)
        #Zeit_pause(0.7)
        Chat(Chat_Text)
        Fill_Text_datei(Raid_log_dir, Chat_Text+"\n", "a")

        Zeit_pause(0.5)

        time.sleep(0.05)
    time.sleep(0.01)

pyautogui.alert("Es wurden alle Pins Eingegeben")

####################################################################################################