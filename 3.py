from tkinter import*
root=Tk()
# button without any function
mybutton=Button(root,text="click me")
mybutton.pack()
# state disabled button
mybutton1=Button(root, text="click", state=DISABLED)
mybutton1.pack()
# buton x and y padding
mybutton2=Button(root, text="click", padx=50)
mybutton2.pack()
mybutton3=Button(root, text="click", padx=50)
mybutton3.pack()
root.mainloop()