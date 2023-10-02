####################################################################################################
# #   Intro

v = "1.0.3"
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
        return Raid_List , False
    else:
        print ("\nEs wurden folgende gespeicherten CodeLock Raids gefunden:\n >>> "+ str(Raid_List)+"\n")
    return Raid_List, True

def List_to_Text (List):
    List_2 = List.copy()
    List_2.sort(reverse=True)
    List_2_text =""
    List_2_len = len(List)
    x = List_2_len + 1
    while True:
        x = x - 1
        if x == 0 :
            break
        Item = List_2.pop()
        List_2_text = List_2_text + " » " + str(Item)+"\n"
    return List_2_text

def Raid_cheack(Raid_List, Raid_List_Text):
    if Raid_List[1] == False:
        #Raid_Name = input("Wie soll dein Raid heißen: \n>>> ")
        Raid_Name = pyautogui.prompt(text='Wie soll dein Raid heißen?', title='Neuen Raid Erstellen' , default='CodeLock-Raid-1')
    
    else:
        #Raid_Name = input("Gebe gespeicherten Code Lock Raid Namen ein oder einen Namen für einen Neuen Code-Lock Raid: \n >>> " )
        Raid_Name = pyautogui.prompt(text="""Öffne einen Vorhandenen Raid oder erstelle einen neuen.
        
        Es wurden folgende gespeicherten CodeLock Raids gefunden:\n\n """+ str(Raid_List_Text), title='Raid Öffnen' , default='CodeLock-Raid-1')

    print("Es wurde Folgender Raid geöffnet/erstellt: >>> [" +str(Raid_Name)+"] <<<\n")
    if Raid_Name in Raid_List[0]:
        return Raid_Name, 0, 10000, False
    else:
        Code_Start = int(pyautogui.prompt(text='Code Raid Start an Stelle: (1-10000)', title='Code Start Position' , default='1'))
        print("Code Liste startet an Stelle: " + str(Code_Start))
        Code_Ende = int(pyautogui.prompt(text='Code Raid Ende an Stelle: (2-10000)', title='Code Start Position' , default='10000'))
        print("Code Liste endet an Stelle: " + str(Code_Ende))
        x_Raid_Folder = Folder_gen( Raid_Name, "Documents/Rust - Key-Bot/Raid-List" )   # Main Folder erstellen
        return Raid_Name, Code_Start, Code_Ende, True

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
            print("Der HOTKEY: ["+str(hotkey)+"] Funktioniert nur im Game Rust.")
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

def Code_List(Code_Start, Code_Ende, Full_Code_List_dir, Raid_Rest_CodeList_dir):

    Code_Start = Code_Start - 1
    Max = 10000
    Länge = Code_Ende - Code_Start

    Code_Start_pos = (Max - Code_Start)
    Code_Ende_pos = (Max - Code_Ende)

    with open(Full_Code_List_dir) as f:
        data = f.readlines()[ Code_Ende_pos : Code_Start_pos ]

    data.reverse()
    data_len = len(data)

    x = data_len + 1
    while True:
        x = x - 1
        prozent = round(100-((100/data_len)*x),2)
        if x == 0:
            print("\nDie CodeLock Liste wurde erstellt >>> ["+str(Raid_Rest_CodeList_dir) + "] <<<\n" )
            break
        Item = data.pop()
        print (str(prozent)+ "% - [" +str(Item[0:4])+"]")
        Fill_Text_datei(Raid_Rest_CodeList_dir, Item, "a")

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
Full_Code_List_dir = file_path + "/Full Code List 10000.txt"

Main_Folder = Folder_gen( "Rust - Key-Bot","Documents" )   # Main Folder erstellen
Raid_List_Folder = Folder_gen( "Raid-List","Documents/Rust - Key-Bot" )   # Raid Folder erstellen

print(f0)
Raid_List = Raid_List(Raid_List_Folder)

List_for_text = Raid_List[0]
Raid_List_Text = List_to_Text (List_for_text)

Raid_config = Raid_cheack(Raid_List, Raid_List_Text)
Raid_Name = Raid_config[0]
Code_Start = (Raid_config[1])
Code_Ende = (Raid_config[2])
Raid_New = Raid_config[3]
Raid_Folder = Raid_List_Folder + "/" + Raid_Name
Code_Listen_länge = (Code_Ende+1)-Code_Start

if Raid_New == True:
    datei_Date = Date_Time=(time.strftime("%d_%m-%Y-%H:%M"))
    Raid_log_dir = Erstelle_TextDatei( Raid_Name , Raid_Folder, f0 )
    f1 = "\n Der CodeLock Raid ["+Raid_Name +"] wurde erstellt am "+ str(datei_Date)+"\nEs werden "+str(Code_Listen_länge)+" von 10000 Code Möglichkeiten abgefragt./nDie Code Liste startet ab Code Nr ["+str(Code_Start)+" bis "+str(Code_Ende+1) +"]\n\n ############################################################\n\nEingegebene Codes (STRG + F Um nach einem Code zu suchen):\n\n"
    Fill_Text_datei(Raid_log_dir, f1, "a")
    Raid_Rest_CodeList_dir = Erstelle_TextDatei( "Code List" , Raid_Folder,"" )
    Code_List(Code_Start, Code_Ende, Full_Code_List_dir, Raid_Rest_CodeList_dir)

else:
    Raid_log_dir = os.path.join(Raid_Folder+"\\"+Raid_Name+".txt")     # Path + text datei name

hotkey = pyautogui.prompt(text="Ändere bei bedraf den HOTKEY um den CodeLock zu öffnen.", title='HotKey Einstellung' , default='alt + E')
print ("Der HotKey um in Rust den Code einzugeben liegt auf ["+str(hotkey)+"]\n")

print("Stelle den In Game-Chat mit [Enter] und dann [TAB] auf Teamchat um.\n")
pyautogui.alert("Stelle den In Game-Chat mit [Enter] und dann [TAB] auf Teamchat um.")
print("Öffne nun in Game einen Code Lock und Drücke [" +(hotkey) + "] um den Code Automatsich einzugeben!")
pyautogui.alert("Öffne nun in Game einen Code Lock und Drücke ["+str(hotkey)+"] um den Code Automatsich einzugeben!")

###################################

####################################################################################################
#Main Programm

Caps_Lock_off()

start_time_Z = time.time()+1

Z = 1
while True:

    if keyboard.is_pressed(hotkey):
        Caps_Lock_off()
        
        Rust = that_window_pos("Rust")
        if Rust == False:
            continue
        else :

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
                Restlänge = Code_Listen_länge-total_lines
                Prozent = (100/Code_Listen_länge)*Restlänge
                Prozent = round(Prozent, 2)

                Pin_pro_min = (Z/elapsed_time_Z)
                Time_for_10k = round((((1/Pin_pro_min)*total_lines))/60,2)
                Pin_pro_min = round(Pin_pro_min,3)
            Caps_Lock_off()
            Chat_Text = ">>" + str(Pin) + "<< | [" + str(Code_Listen_länge-1 - total_lines) + "/" +str(Code_Listen_länge-1) +   "]Pins | [" + str(Pin_pro_min) + "]Pin/min | Zeit bis 100% : ["+str(Time_for_10k) + "]h | Fortschritt : [" + str(Prozent)+"/100]%"
            print("\n"+Chat_Text)
            Eingabe(Pin)
            #Zeit_pause(0.7)
            Chat(Chat_Text)
            Fill_Text_datei(Raid_log_dir, Chat_Text+"\n", "a")

        Zeit_pause(0.5)

        time.sleep(0.05)
    time.sleep(0.01)

print("Es wurden alle Pins Eingegeben")
pyautogui.alert("Es wurden alle Pins Eingegeben")

####################################################################################################