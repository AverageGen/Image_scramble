from tkinter import *
from PIL import Image, ImageTk
import random
from tkinter import messagebox
import os



def encrypt(entry):
    count = 0
    img_path = entry
    img = Image.open(img_path)
    exifdata = img.getexif()
    width, height = img.size
    mode = img.mode
    pixel_map = img.load()
    seed = random.randrange(1, 4000)

    exist_value = exifdata.get(271)

    if exist_value != "eug_imagescrambler":
        exifdata[270] = seed
        exifdata[271] = "eug_imagescrambler"
        
    elif exifdata[271] == "eug_imagescrambler":
        messagebox.showerror("Erro", "Arquivo já foi encriptado ou aconteceu algo de errado")

    shuffled_list = [[(0,0,0)]* height for i in range(width)]
    pixel_list = [[(0,0,0)] * height for i in range(width)]

    for x in range(width):
        for y in range(height):
            pixel_list[x][y] = pixel_map[x, y]


    for i in range(width):
        indices = list(range(len(shuffled_list[i])))
        random.seed(seed+i)
        random.shuffle(indices)

        shuffled_list[i] = [pixel_list[i][j] for j in indices]

    modified_image = Image.new(mode, (width, height))

    modified_pixel_map = modified_image.load()

    for x in range(width):
        for y in range(height):
            modified_pixel_map[x, y] = shuffled_list[x][y]



    modified_image.show()
    modified_image.save("modified_img.png", exif=exifdata)
    messagebox.showinfo("Operação Completa", "Foto Completa")
    




 





def decrypt(entry):
    
    
    img_path = entry
    img = Image.open(img_path)
    exifdata = img.getexif()
    width, height = img.size
    mode = img.mode
    pixel_map = img.load()

    exist_value = exifdata.get(271)

    if exist_value != "eug_imagescrambler":
        messagebox.showerror("Erro", "Arquivo não foi encriptado ou aconteceu algo de errado")



    seed = int(exifdata[270])

    pixel_list = [[(0,0,0)] * height for i in range(width)]
    unshuffled_list = [[(0,0,0)] * height for i in range(width)]

    for x in range(width):
        for y in range(height):
            pixel_list[x][y] = pixel_map[x,y]


    for i in range(width):
        shuffled_indices = list(range(len(pixel_list[i])))
        random.seed(seed+i)
        random.shuffle(shuffled_indices)
        unshuffled_list[i] = [pixel_list[i][shuffled_indices.index(j)] for j in range(len(pixel_list[i]))]

    unmodified_image = Image.new(mode, (width, height))
    unmodified_pixel_map = unmodified_image.load()

    for x in range(width):
        for y in range(height):
            unmodified_pixel_map[x, y] = unshuffled_list[x][y]


    unmodified_image.show()
    messagebox.showinfo("Operação Completa", "Foto Completa")







def submit(mode, entry):

    if not os.path.isfile(entry):
        messagebox.showerror("Erro", "O arquivo não foi encontrado.")

    if mode == 0:
        encrypt(entry)
        print("encrypt")
    elif mode == 1:
        print("decrpyt")
        decrypt(entry)

    


def main():
    root = Tk()
    root.title("Image scrambler")
    root.geometry('600x300')

    entry = Entry(root, width=50)
    entry.pack()

    submit_button = Button(root, text="Submit", command=lambda:submit(mode.get(), entry.get()))
    submit_button.pack()

    img1 = Image.open('Icons/aberto.png').resize((50, 50))
    img2 = Image.open('Icons/fechado.png').resize((50, 50))


    aberto = ImageTk.PhotoImage(img1)
    fechado = ImageTk.PhotoImage(img2)

    mode = BooleanVar()
    mode.set(0)

    radio1 = Radiobutton(root, text='encrypt', image=aberto, compound='left',variable=mode , value=0)
    radio2 = Radiobutton(root, text='decrypt', image=fechado, compound='left',variable=mode ,  value=1)

    radio1.pack()
    radio2.pack()
                    


    root.mainloop()



main()




