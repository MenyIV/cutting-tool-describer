from tkinter import *
import tkinter as tk
from data import tooldata

#Dle výběru z list menu to vypíše volby
#data jsou v data.py


#obrázky
# zadávací pole
#vyřešit ten bordel

#tlačítko PUBLISH



# Create the app's main window
window = tk.Tk()


window.title("testing")
window.geometry("520x300")
window.option_add('*Font', 'Verdana 10')





#tohle je potřeba upravit aby to vyrobil list N1,N2,N3,

def skupiny():
    list = []
    for each in tooldata:
        print(each)
        list.append(each)
    return(list)
mach_tools_list = skupiny()        

def handle_button_press():
    window.destroy()
    
def printInput(): 
    inp = inputtxt.get(1.0, "end-1c") 
    lbl.config(text = "Provided Input: "+inp)

ix=20
iy=2
def inputtxt(ix,iy):
    #funkce která vykreslí zadávací pole    -NEFUNGUJE
        inputtxt = tk.Text(window, 
                   height = 5, 
                   width = 20)
        inputtxt.pack()
    
def callback (hodnota):
    #Vypisování nabídek a zadávacích polí
    # není moc chytrý to řetězit do funkce :-)
    variable.set(hodnota)
    #print (f"hodnota je:", variable.get(), variable)
    print(variable.get())
    ix=20
    iy=2
    r=1
    tabulka=tk.Label()
    tabulka.option_add('*Font', 'Verdana 10') 
    
    for each in (tooldata[variable.get()]):
        #tohle by mělo smazat ten bordel mezi čísly
        #vyřešit ten bordel mezi čísly
        # asi if change clear monitor nebo tak něco

        Label(tabulka, text=(each)).grid(row=r)
        Label(tabulka, text=u"").grid(row=r)
        e1 = Entry(tabulka)
        e2 = Entry(tabulka)
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        
        r+=1
        
        
        
        
        
        #funkční výpis pomocí packu
        #nadpis=Label(window,text=("")).place(x=ix,y=iy)
        #nadpis=Label(window,text=(each)).place(x=ix,y=iy)
        #inputtxt(ix,iy)  #TADY jsem si to rozbil
        
        
        #nadpis.pack()#padx=ix,pady=iy,side=tk.LEFT))
                #zadávací pole
                
        #výpočet posunutí na další řádek
        ix=ix
        iy=iy+20
        

        
        

#Listovací MENU
variable = StringVar(window)
variable.set(mach_tools_list[0]) # default value
w = OptionMenu(window, variable, *mach_tools_list, command=callback)
w.pack()
print(w)
####################################################################














#EXIT button
button = tk.Button(text="EXIT", command=handle_button_press)#.place(x=260,y=250)
button.pack(side="bottom")




lbl = tk.Label(window, text = "") 
lbl.pack() 


# Start the event loop
window.mainloop()