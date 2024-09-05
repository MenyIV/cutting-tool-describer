import tkinter as tk

list_num=["1","2","3"]

def button_callback(list_num):
    for i in list_num:
        user_input = i.get()
        print("User input:", user_input)

root = tk.Tk()

r=0
for i in list_num:
    i = tk.Entry(root)
    i.grid(row=r, column=4, padx=10, pady=10)
    r+=1
    

button = tk.Button(root, text="Submit", command=button_callback(list_num))
button.grid(row=5, column=4, padx=10, pady=10)

root.mainloop()