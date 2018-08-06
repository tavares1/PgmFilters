import numpy
from PIL import Image


def threshold_filter(data,limiar):
    # Criando um novo np.ndarray, estrutura cedida pelo numpy que simula uma matriz em python.
    data_final = data
    for i in range(len(data)):
        for j in range(len(data[i])):
            # Caso a intesidade de preto daquele pixel seja maior que o limiar, o valor dela na nova imagem será 255, caso contrário 0
            data_final[i][j] = 255 if data[i][j] > limiar else 0
    return data_final


def main():
    img = Image.open("../images/whitmore.pgm")
    arr = numpy.array(img)
    threshold = threshold_filter(arr,95)
    out = Image.fromarray(threshold)
    img.show()
    out.show()


main()
