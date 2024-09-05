#obrázky a pole pro zadání to kreslí

#nějak zpracovat ty zadané hodnoty z těch políček
#enteries append a po kliku zapiuč projde vřechny řádky a prostě to pozbírá?
#nějaký nástřel je na path.py nebo zde:https://discuss.python.org/t/using-values-from-multiple-entry-box-in-tkinter/20796/4


#nabrat poslední číslo z excelového sešitu (pandas)




import tkinter as tk
from data import tooldata
from data import tool_program_data
from tkinter import *
from PIL import Image, ImageTk
import os
from pathlib import Path

root = tk.Tk()
root.title("Tabulka s listovacím menu")
root.option_add('*Font', 'Verdana 10') 
root.geometry("650x700")

values=[]

def fetch_entries(each_list):
    #tady to vezme hodnotu ze druhého sloupce a vytvoří dictionary s hodnotou dalšího sloupce
    #for each in values:
    print(each_list)
    r=0
    hodnoty=[]
    for each in (each_list):

        print(f"získání hodnot{each}")
        hodnoty.append(entry.get(row=r,column=3))

def skupiny():
    list = []
    for each in tooldata:
        print(each)
        list.append(each)
    return(list)
mach_tools_list = skupiny()    

def handle_button_press():
    root.destroy()
    
def clear_values():
    #vymaže tabulku od row0;column1 až do row20 column20
    for labels in root.grid_slaves():
        if 0 < int(labels.grid_info()["row"]) < 20 and 1 < int(labels.grid_info()["column"]) < 20:
            labels.grid_forget()
        else:
            pass

def callback (value):
    print(f"Vybráno: {value}")
    clear_values()
    
    #najde a nalepí obrázek
    picture = picture_path(tool_program_data[value])
    label = tk.Label(root, image=picture)
    label.image = picture  # Udržujeme odkaz na objekt PhotoImage
    label.grid(row=10, column=3)  # Zobrazíme obrázek v mřížce
    each_list=[]
    r=0
    for each in (tooldata[value]):
        button = tk.Label(text=each,)
        button.grid(row=r, column=3, padx=10, pady=10)
        entry = tk.Entry()
        entry.grid(row=r, column=4, padx=10, pady=10)
        each_list.append(each)
        #print(each_list)
        r+=1
        # Tlačítko pro získání vybrané hodnoty
    #button = tk.Button(root, text="Zapiš", command=lambda: fetch_entries(each_list))
    #button.grid(row=2, column=0, padx=10, pady=10)
        
    return(each_list)


def picture_path(properties):
    #vrací cestu k obrázku nástroje dle parametrů z data.py
    
    #properties jsou takovýto dictionary
    #{'picture_name': 'drill', 'picture_suffix': '.png', 'picture_category': 'pic_mill_tool'}
    
    current_directory = os.path.dirname(os.path.abspath(__file__))
    tool_category = properties["picture_category"]
    tool_type = properties["picture_name"]
    suffix = properties["picture_suffix"]
    #tool_type = tool_type+suffix
    full_path = os.path.join(current_directory, tool_category,tool_type+suffix)
    
    #nakonec otevře a vrátí obrázek

    return ImageTk.PhotoImage(Image.open(full_path))

def seznam_prvku(vyber):
    seznam = []
    for i in (tooldata[vyber]):
        seznam.append(i)
    return (seznam)

def vypsat():
    for entry in entries:
        print(entry.get())

# Možnosti pro listovací menu
OPTIONS = mach_tools_list

# Výchozí hodnota
selected_option = tk.StringVar(root)
selected_option.set(OPTIONS[0])

# Vytvoření listovacího menu
option_menu = tk.OptionMenu(root, selected_option, *OPTIONS)
option_menu.grid(row=0, column=0, padx=10, pady=10)

# Tlačítko pro získání vybrané hodnoty

button = tk.Button(root, text="OK", command=lambda: callback(selected_option.get()))
button.grid(row=1, column=0, padx=10, pady=10)

entries = callback(selected_option.get())
print(f"Parametry jsou {entries}")


button = tk.Button(text="Zapis", command=vypsat)#.place(x=260,y=250)
button.grid(row=2, column=0, padx=10, pady=10)



button = tk.Button(text="EXIT", command=handle_button_press)#.place(x=260,y=250)
button.grid(row=50, column=3, padx=10, pady=10)


root.mainloop()