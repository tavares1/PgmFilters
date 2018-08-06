import numpy
from PIL import Image


def constrat(data,value_contrast):
    data_final = data
    # Conhecendo o tamanho da imagem.
    height, width = data.shape
    for x in range(0, height):
        for y in range(0, width):
            # Calculando o valor máximo de contraste do pixel, caso o valor calculado seja maior que 255, retornamos o 255, valor máximo do pixel.
            max_contrast = data[x][y] + data[x][y] * 10 / 100 if data[x][y] + data[x][y] * 10 / 100 < 255 else 255
            # Calculando o valor mínimo de contraste do pixel, caso o valor calculado seja menor que 0, retornamos 0, valor minimo.
            min_contrast = data[x][y] - data[x][y] * 10 / 100 if data[x][y] - data[x][y] * 10 / 100 > 0 else 0
            # Caso o valor do pixel, seja menor que o valor limiar de contraste, retornamos o valor minimo de contraste, senão retornamos o valor máximo.
            data_final[x][y] = min_contrast if data[x,y] < value_contrast else max_contrast
    # Retornando o np.ndarray, um array com esteroides fornecido pelo numpy.
    return data_final


def main():
    img = Image.open("../images/abe_natsumi.pgm")
    arr = numpy.array(img)
    arr_filtred = constrat(arr,180)
    out = Image.fromarray(arr_filtred)
    img.show()
    out.show()


main()