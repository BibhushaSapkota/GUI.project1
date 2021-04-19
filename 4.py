from tkinter import*
root=Tk()
def myClick():
    mylabel=Label(root, text="Button is clicked!!")
    mylabel.pack()
myButton=Button(root, text="Click Me!", command=myClick)
myButton.pack()
root.mainloop()
