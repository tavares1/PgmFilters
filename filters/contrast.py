import numpy
from PIL import Image


def constrat(data,value_contrast):
    data_final = data
    height, width = data.shape
    for x in range(1, height - 1):
        for y in range(1, width - 1):
            max_constract = data[x, y] + data[x, y] * 10 / 100
            min_constract = data[x, y] - data[x, y] * 10 / 100
            if max_constract > 255:
                max_constract = 255
            if min_constract < 0:
                min_constract = 0
            if data[x, y] < value_contrast:
                data_final[x, y] = min_constract
            else:
                data_final[x, y] = max_constract

    return data_final


def main():
    img = Image.open("../images/abe_natsumi.pgm")
    arr = numpy.array(img)
    arr_filtred = constrat(arr,200)
    out = Image.fromarray(arr_filtred)
    img.show()
    out.show()


main()