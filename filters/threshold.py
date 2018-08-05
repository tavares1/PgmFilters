import numpy
from PIL import Image


def threshold_filter(data,limiar):
    data_final = numpy.zeros((len(data),len(data[0])))
    for i in range(len(data)):
        for j in range(len(data[i])):
            value = 255 if data[i][j] > limiar else 0
            data_final[i][j] = value
    return data_final


def main():
    img = Image.open("../images/whitmore.pgm")
    arr = numpy.array(img)
    removed_noise = threshold_filter(arr,150)
    out = Image.fromarray(removed_noise)
    img.show()
    out.show()


main()