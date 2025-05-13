from PIL import Image, ImageFilter
import random
import sys

def encrypt(height, width, mode, pixel_list):
    img_path = sys.argv[1]
    img = Image.open(img_path)
    exifdata = img.getexif()
    seed = random.randrange(1, 4000)
    exifdata[270] = seed
    exifdata[271] = "eug_imagescrambler"
    
    shuffled_list = [[(0,0,0)]* height for i in range(width) ]

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







def decrypt(height, width, mode, pixel_list, exifdata):
    seed = int(exifdata[270])
    img_path = sys.argv[1]
    img = Image.open(img_path)
    unshuffled_list = [[(0,0,0)] * height for i in range(width)]

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


    
    


def main():
    img_path = sys.argv[1]
    img = Image.open(img_path)
    width, height = img.size
    mode = img.mode
    pixel_map = img.load()
    exifdata = img.getexif()
    if not exifdata[271]:
        exifdata[271] = 0
    make = exifdata[271]
    pixel_list = [[(0,0,0)] * height for i in range(width)]

    for x in range(width):
        for y in range(height):
            pixel_list[x][y] = pixel_map[x, y]


    if make != "eug_imagescrambler":
        encrypt(height, width, mode, pixel_list)
    else:
        decrypt(height, width, mode, pixel_list, exifdata)



main()
