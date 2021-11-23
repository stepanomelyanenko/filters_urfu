from PIL import Image
import numpy as np

def convert_image_to_mosaic(img_in="img2.jpg",
                            img_out="res.jpg",
                            block_size=10,
                            gradation_step=50):
    img = Image.open(img_in)
    img_arr = np.array(img)
    for width in range(0, len(img_arr), block_size):
        for height in range(0, len(img_arr[1]), block_size):
            brightness = np.sum(img_arr[width: width + block_size, height: height + block_size]) \
                        // (block_size * block_size * 3)
            brightness -= brightness % gradation_step
            img_arr[width: width + block_size, height: height + block_size] = np.full(3, brightness)

    return Image.fromarray(img_arr).save(img_out)

convert_image_to_mosaic()
"""
img = Image.open("img2.jpg")
arr = np.array(img)
a = len(arr)
a1 = len(arr[1])
i = 0
while i < a - 11:
    j = 0
    while j < a1 - 11:
        s = 0
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                n1 = arr[n][n1][0]
                n2 = arr[n][n1][1]
                n3 = arr[n][n1][2]
                M = n1 + n2 + n3
                s += M
        s = int(s // 100)
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                arr[n][n1][0] = int(s // 50) * 50
                arr[n][n1][1] = int(s // 50) * 50
                arr[n][n1][2] = int(s // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')
"""
