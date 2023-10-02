"""
Use: - from util.__funktion__ import *

ChatGPT promt for docstrgs:

In copy code mode,

write me a .py docstr ("""""") with the content:
Args, Returns and Example Usage.
For Args and Returns create a list with "- ".
and for Example Usage create a list with ">>>  ".
Here is the code:


"""

import logNow
from logNow import log
import os
from configparser import ConfigParser
import shutil
import time
import sys
import pyautogui
import win32api
import win32con
from win32gui import FindWindow, GetWindowRect


def new_path(base_path, *components):
    """
    Combines paths based on a base and optional components.

    Args:
        base_path (str): The base path.
        *components (str): Any number of components to combine.

    Returns:
        str: The combined and normalised path.
    """
    # Normalize the base path
    base_path = os.path.normpath(base_path)

    # Combine the components into a single path
    combined_path = os.path.join(base_path, *components)

    # Normalize and return the combined path
    return os.path.normpath(combined_path)

def read_config(config_dir, section, option, arg=None):
    """Reads a configuration file and returns the specified value as the desired data type.

Args:
- config_dir (str): The directory where the configuration file is located.
- section (str): The section of the configuration file where the option is located.
- option (str): The option to retrieve from the configuration file.
- arg (str, optional): The desired data type of the retrieved value. Can be "float", "int", or "tuple". Defaults to None.

Returns:
- If arg is not provided: the value of the specified option as a string.
- If arg is "float": the value of the specified option as a float.
- If arg is "int": the value of the specified option as an integer.
- If arg is "tuple": the value of the specified option as a tuple of integers.

Example Usage:
>>> read_config("config.ini", "database", "port")
'5432'

>>> read_config("config.ini", "database", "port", "int")
5432

>>> read_config("config.ini", "database", "credentials", "tuple")
(123456, 'password')
"""

    if arg == "float":
        config = ConfigParser()
        config.read(config_dir)
        load_config = (config[section][option])
        config_float = float(load_config)
        log(f"Config loaded: [ ({option})  = ({config_float}) ] conv to float", "g")

        return config_int
    if arg == "int":
        config = ConfigParser()
        config.read(config_dir)
        load_config = (config[section][option])
        config_int = int(load_config)
        log(f"Config loaded: [ ({option})  = ({config_tuple}) ] conv to int", "g")

        return config_int

    if arg == "tuple":
        config = ConfigParser()
        config.read(config_dir)
        load_config = (config[section][option])
        config_tuple = tuple(map(int, load_config.split(",")))
        log(f"Config loaded: [ ({option})  = ({config_tuple}) ] conv to tuple", "g")

        return config_tuple

    else:
        config = ConfigParser()
        config.read(config_dir)
        load_config = (config[section][option])

        log(f"Config loaded: [ ({option})  = ({load_config}) ]", "g")

        return load_config


def write_config(config_dir, section, Key, option):
    """
Args:
    - config_dir (str): The directory where the configuration file is located.
    - section (str): The section name in the configuration file.
    - Key (str): The key to update or add in the specified section.
    - option (str): The value to assign to the specified key.

Returns:
    - None

Example Usage:
    - Updating an existing key in a section of a configuration file
    >>>  write_config('config.ini', 'section1', 'key1', 'new_value')

    >>>  Adding a new key in a section of a configuration file
    >>>  write_config('config.ini', 'section2', 'key2', 'value2')
"""
    config = ConfigParser()
    # update existing value
    config.read(config_dir)
    try:
        config.add_section(section)
    except:
        pass
    config.set(section, Key, option)  # Updating existing entry
    with open(config_dir, 'w') as configfile:
        config.write(configfile)
    print(
        f"\nChange settings -> {config_dir}\n[{section}]\n{Key}) = {option}\n")


def Folder_gen(Folder_Name, Folder_dir):
    """Creates a new folder if it does not already exist.

            Args:
            - folder_name (str): The name of the folder to be created.
            - folder_dir (str): The directory in which the folder is to be created.

            Returns:
            - str: The full path of the created folder.

            Example usage :
            >>> Folder_Name = "my_folder"
            >>> Folder_dir = "path/to/parent/directory"
            >>> created_folder_path = Folder_gen(Folder_Name, Folder_dir)
            >>> print("Created folder path:", created_folder_path)
    """

    print("Folder structure is checked and created if necessary...\n")
    folder = Folder_Name
    # Specifies desired file path
    #dir = "~/"+str(Folder_dir)+"/"+str(folder)
    full_path = Folder_dir + os.path.sep + Folder_Name
    # Adds file path with PC user name
    #full_path = os.path.expanduser(dir)
    # Checks file path for exsistance Ture/False
    if os.path.exists(full_path):
        print("Folder structure already exists")
        print("  ->   " + str(full_path))
    else:                                               # Creates folder if not available
        os.makedirs(full_path)
        log(f"The folder [{folder}] was created in the directory:\n  ->   {full_path}", "b")
        print("\n")
    return(os.path.normpath(full_path))


def Create_File(File_name, save_path, Inhalt):
    """Creates a new text file if it does not already exist and fills it with the specified content.

    Args:
    - File_name (str): The name of the text file.
    - save_path (str): The path where the text file should be saved.
    - Content (str): The content to be written to the text file.

    Returns:
    - str: The complete path of the created text file.

    Example usage:
    >>> file_name = "my_text_file.txt"
    >>> save_path = "/path/to/save/directory"
    >>> content = "This is the content of my text file."
    >>> created_file_path = Create_File(file_name, save_path, content)
    >>> print(created_file_path)
    '/path/to/save/directory/my_text_file.txt'
    """

    complete_Path_Text = save_path + os.path.sep + File_name
    if os.path.exists(complete_Path_Text):
        return complete_Path_Text
    else:
        # Create file
        file1 = open(complete_Path_Text, "w", encoding='utf-8')
        # toFile = input("Write what you want into the field")                   # File input def.
        # File is filled with input
        file1.write(f"{Inhalt}")
        file1.close()
        log(f"\nfile [{File_name}] is created...with conetnt:\{Inhalt}", "b")
        return complete_Path_Text


def Read_File_Out(dir):
    """
    Reads the contents of a file located at the given directory path and returns it as a string.

    Args:
    - dir (str): The directory path of the file to be read.

    Returns:
    - content (str): The contents of the file as a string.

    Example usage:
    >>> file_path = "/path/to/file.txt"
    >>> content = Read_File_Out(file_path)
    >>> print(content)
    'This is the content of the file.'
    """
    with open(dir, 'r', encoding='utf-8') as f:
        content = f.read()

    return content


def copy_image(source_file, dest_file) -> None:
    """Copies an image file from the source path to the destination path.

    Args:
    - source_file (str): The path of the image file to be copied.
    - dest_file (str): The path where the image file should be copied to.

    Returns:
    - file (str) full path of the img

    Raises:
    - IOError: If an error occurs while copying the file.

    Example usage:
    >>> source_path = "/path/to/source/image.jpg"
    >>> dest_path = "/path/to/destination/image.jpg"
    >>> copy_image(source_path, dest_path)
    '/path/to/destination/image.jpg'
    """
    try:
        shutil.copy(source_file, dest_file)
        file = dest_file
        log(f"Image [{file}] successfully copied!", "b")
        return file
    except IOError as e:
        log(f"Error when copying the file: {e}", "r")


def File_name_with_time(FileName):
    """Generate a filename with a timestamp.

    Args:
    - FileName (str): The name of the file.

    Returns:
    - FullName (str): The full name of the file with a timestamp in the format of "FileName-DD_MM_YYYY-HH.MM".

    Example usage:
    >>> Datei_name_mit_Zeit("report")
    'report-04_04_2023-15.30'
    """
    Date = Date_Time = (time.strftime("%d_%m-%Y-%H.%M")
                        )        # Generates date formater
    # Generates file name
    FullName = (FileName+"-"+(Date))
    return FullName


def TimeStemp():
    """
    Generates a timestamp string in the format of "dd_mm-yyyy_HH:MM:SS".

    Args:
        None

    Returns:
        A string representing the current date and time in the format "dd_mm-yyyy_HH:MM:SS".

    Example Usage:
        >>> TimeStemp()
        '04_04-2023_11:22:33'
    """
    TimeStemp = Date_Time = (time.strftime("%d_%m-%Y_%H:%M:%S"))
    return TimeStemp


def cheack_config(default_long_Str):
    """
    Generate a config file path in the 'cfg' directory of the current main file's directory.

    Args:
    - default_long_Str (str): A long string representing the default configuration

    Returns:
    - config_path (str): The absolute path to the generated config file

    Example Usage:
    >>> default_config = "This is the default configuration"
    >>> check_config(default_config)
    '/path/to/main_dir/cfg/config.ini'
    """
    main_file = sys.modules['__main__'].__file__
    main_dir = os.path.dirname(main_file)
    config_path = Folder_gen("cfg", main_dir)
    config_path = Create_File("config.ini", config_path, default_long_Str)
    return config_path


if __name__ == "__funktion__":
    log("__function should not be executed when the file is imported as a module.\nThis was not the case!", "r")
else:
    cheack_config("""[Test]
    abc = 123""")

################################################################################################################################
# def spez.


def Raid_List(Raid_Folder):     # Schaut nach Base ornder
    Raid_List = []

    for file in os.listdir(Raid_Folder):
        Raid_List.append(file)

    Raid_List_Len = len(Raid_List)
    if Raid_List_Len == 0:
        print("Es wurden keine gespeicherten Code-Lock-Raids gefunden. Starten sie einen Neuen!\n")
        return Raid_List, False
    else:
        print("\nEs wurden folgende gespeicherten CodeLock Raids gefunden:\n >>> " +
              str(Raid_List)+"\n")
    return Raid_List, True


def List_to_Text(List):
    List_2 = List.copy()
    List_2.sort(reverse=True)
    List_2_text = ""
    List_2_len = len(List)
    x = List_2_len + 1
    while True:
        x = x - 1
        if x == 0:
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


def Fill_Text_datei(Datei_dir, Fill, Atribut):
    # Datei erstellen
    file1 = open(Datei_dir, Atribut)
    # Datei wird gefüllt mit input
    file1.write(str(Fill))
    file1.close()
    #print ("Die Text Datei >>> ["+ str(Datei_dir)+"] wurde beschreiben.")


def Code_List(Code_Start, Code_Ende, Full_Code_List_dir, Raid_Rest_CodeList_dir):

    Code_Start = Code_Start - 1
    Max = 10000
    Länge = Code_Ende - Code_Start

    Code_Start_pos = (Max - Code_Start)
    Code_Ende_pos = (Max - Code_Ende)

    with open(Full_Code_List_dir) as f:
        data = f.readlines()[Code_Ende_pos: Code_Start_pos]

    data.reverse()
    data_len = len(data)

    x = data_len + 1
    while True:
        x = x - 1
        prozent = round(100-((100/data_len)*x), 2)
        if x == 0:
            print(
                "\nDie CodeLock Liste wurde erstellt >>> ["+str(Raid_Rest_CodeList_dir) + "] <<<\n")
            break
        Item = data.pop()
        print(str(prozent) + "% - [" + str(Item[0:4])+"]")
        Fill_Text_datei(Raid_Rest_CodeList_dir, Item, "a")


def Caps_Lock_off():
    caps_status = 0
    caps_status = win32api.GetKeyState(win32con.VK_CAPITAL)
    if caps_status == 0:
        caps_status
    else:
        time.sleep(0.1)
        print('CapsLock is on')
        pyautogui.press('capslock')
        time.sleep(0.1)


def that_window_pos(window_name):

    # FindWindow takes the Window Class name (can be None if unknown), and the window's display text.

    while True:
        try:
            window_handle = FindWindow(None, window_name)
            window_rect = GetWindowRect(window_handle)
            break
        except:
            print(" Das Fenster >>> "+str(window_name) +
                  " <<< konnte nicht gefunden werden")
            window_rect = False
            print("Der HOTKEY Funktioniert nur im Game Rust.")
            pyautogui.alert("Der HOTKEY Funktioniert nur im Game Rust.")
            break

    #print("Das Fenster >> "+ str(window_name) + "<<< ist auf pos > "+ str(window_rect))
    #(0, 0, 800, 600)
    return window_rect


def next_code(Code_path):

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

    w = open(Code_path, 'w')
    w.writelines([item for item in lines[:-1]])
    w.close()
    return Next_Code


def Eingabe(Eingabe):
    Caps_Lock_off()
    time.sleep(0.5)
    pyautogui.write(Eingabe, interval=0.05)
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(0.1)


def Chat(Eingabe):
    Caps_Lock_off()
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.1)
    pyautogui.write(Eingabe, interval=0.00)
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(0.1)