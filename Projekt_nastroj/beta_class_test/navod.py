# -*- coding: utf-8 -*- 
from tkinter import *
from data import tooldata

def skupiny():
    list = []
    for each in tooldata:
        print(each)
        list.append(each)
    return(list)
mach_tools_list = skupiny()    

def overeni():
    print ("nyni overuji text")
    return 1

def cteni():
    for each in (mach_tools_list):
        print (each.get())
        print (eachObsah.get() ) # pristup pres tkPromennou
        #print (each.get())     # pristup pres metodu get instance Entry

hlavni = Tk()
hlavni.option_add('*Font', 'Arial 9')  # aby byl lepsi font

for each in (mach_tools_list):
    eachObsah=StringVar()
    eachObsah.set("Žluťoučký kůň pěl ďáleské ódy.")

# obsah je napojen na tkProměnnou vstupObsah 
# a při každém písmení probíhá ověřování
    each = Entry(hlavni, textvariable=eachObsah, width=40, validate="key", 
              validatecommand=overeni)
    each.pack(side=LEFT)
    each.focus_set()           # aby se dalo hned psát
    each.icursor(END)          # aby byl kurzor na konci
    each.selection_range(0, END)
  
tlacitko = Button(hlavni, text=u"přečti", width=10, command=cteni)
tlacitko.pack()

mainloop()