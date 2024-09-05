import tkinter as tk
from data import tooldata
from data import tool_program_data

root = tk.Tk()
root.title("Tabulka s listovacím menu")
root.option_add('*Font', 'Verdana 10') 
root.geometry("650x700")

class radek_hodnot:
    
    def __init__(self,each,r):
        text=each
        button = tk.Label(text=text)
        button.grid(row=r, column=3, padx=10, pady=10)
        entry = tk.Entry()
        entry.grid(row=r, column=4, padx=10, pady=10)
        self.vstup=entry.get()
        
        
    def read_value(self):
          print(self.vstup)
    
    
    
    
    
def skupiny():
    list = []
    for each in tooldata:
        print(each)
        list.append(each)
    return(list)

def vycteni_hodnot():
    print ("radek.vstup()")
    


mach_tools_list = skupiny()
print (mach_tools_list)


r=0
for each in (mach_tools_list):
    radek_hodnot(each,r,mach_tools_list)
    r+=1
    
    

button = tk.Button(root, text="OK", command=lambda: vycteni_hodnot())
button.grid(row=5, column=2, padx=10, pady=10)

root.mainloop()

print(button)



    