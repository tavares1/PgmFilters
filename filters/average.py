import numpy
from PIL import Image


def median_filter(data, filter_size):
    temp = []
    indexer = filter_size // 2
    data_final = numpy.zeros((len(data),len(data[0])))
    for i in range(len(data)):

        for j in range(len(data[0])):

            for z in range(filter_size):
                if i + z - indexer < 0 or i + z - indexer > len(data) - 1:
                    for c in range(filter_size):
                        temp.append(0)
                else:
                    if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
                        temp.append(0)

                    else:
                        for k in range(filter_size):
                            temp.append(data[i + z - indexer][j + k - indexer])

            data_final[i][j] = numpy.mean(temp)
            temp = []
    return data_final


def main():
    img = Image.open("../images/whitmore_noise.pgm")
    arr = numpy.array(img)
    removed_noise = median_filter(arr, 3)
    out = Image.fromarray(removed_noise)
    img.show()
    out.show()


main()