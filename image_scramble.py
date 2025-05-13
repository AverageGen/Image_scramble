from PIL import Image, ImageFilter
import random

# carrega a imagem
img = Image.open("2560px-A-Cat.jpg")



seed = 24

widht, height = img.size
mode = img.mode
pixel_map = img.load()

pixel_list=[[(0,0,0)] * height for i in range(widht)] 
shuffled_list=[[(0,0,0)] * height for i in range(widht)] 



# copia os pixels da foto original em uma matriz 2D
for x in range(widht):
    for y in range(height):
        pixel_list[x][y] = pixel_map[x, y]


# emabaralha os pixels e os armazenam na lista embaralhada
for i in range(widht):
    indices = list(range(len(pixel_list[i])))
    random.seed(seed+i)
    random.shuffle(indices)

    shuffled_list[i] = [pixel_list[i][j] for j in indices]
    


modified_image = Image.new(mode, (widht, height))

modified_pixel_map = modified_image.load()

# definem os pixels da imagem modificada
for x in range(widht):
    for y in range(height):
        modified_pixel_map[x, y] = shuffled_list[x][y]



modified_image.show()













