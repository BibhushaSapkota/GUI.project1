from tkinter import*
from PIL import ImageTk, Image

root=Tk()
root.title('image insertion')
my_image=ImageTk.PhotoImage(Image.open("c.png"))
my_label=Label(image=my_image)
my_label.pack()

# Button quit option
button_quit=Button(root,)
button_quit.pack()

root.mainloop()