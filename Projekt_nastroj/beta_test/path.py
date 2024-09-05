import tkinter as tk
ws=tk.Tk()

def fetch():
    global l
    l=[]
    for i in enteries:
        l.append(i.get())
        
        
        
        
enteries=[]
for i in range(8):
    e=tk.Entry(ws)
    e.pack()
    enteries.append(e)
    
(tk.Button(ws,text='ok', command=(fetch))).pack()