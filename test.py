from tkinter import *
from PIL import Image, ImageTk






def submit(mode, entry):
    if mode == 0:
        print("encrypt")
    elif mode == 1:
        print("decrpyt")
    img = Image.open(entry)
    img.show()
    


def main():
    root = Tk()
    root.geometry('600x300')

    entry = Entry(root, width=50)
    entry.pack()

    submit_button = Button(root, text="Submit", command=lambda:submit(mode.get(), entry.get()))
    submit_button.pack()

    img1 = Image.open('aberto.png').resize((50, 50))
    img2 = Image.open('fechado.png').resize((50, 50))


    aberto = ImageTk.PhotoImage(img1)
    fechado = ImageTk.PhotoImage(img2)

    mode = BooleanVar()
    mode.set(0)

    radio1 = Radiobutton(root, text='encrypt', image=aberto, compound='left',variable=mode , value=0)
    radio2 = Radiobutton(root, text='decrypt', image=fechado, compound='left',variable=mode ,  value=1)

    radio1.pack()
    radio2.pack()

    



    root.mainloop()




