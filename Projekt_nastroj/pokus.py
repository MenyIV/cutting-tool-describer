#tohle kupodivu funguje
#je potřeba vrátit list s vytvořenými poli
#a potom tehle list projet for cyklem

from tkinter import *

root=Tk()
entries = []
seznam=["1","2","3"]


def fields(seznam):
    r=0
    for i in seznam:
        en = Entry(root)
        en.grid(row=r+1, column=0)
        entries.append(en)
        r+=1
        
    return(entries)

def hallo():
    for entry in entries:
        print(entry.get())

entries=fields(seznam)
print (entries)
button=Button(root,text="krijg",command=hallo).grid(row=12,column=3)

root.mainloop()