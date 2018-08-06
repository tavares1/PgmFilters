import numpy
from PIL import Image


def median_filter(data, filter_size):
    temp = []
    indexer = filter_size // 2
    data_final = numpy.zeros((len(data),len(data[0])))
    for i in range(len(data)):

        for j in range(len(data[0])):

            for z in range(filter_size):
                # Verificando se estamos na borda, caso sim, colocamos 0 em torno para possibilitar o calculo da mediana.
                if i + z - indexer < 0 or i + z - indexer > len(data) - 1:
                    for c in range(filter_size):
                        temp.append(0)
                else:
                    # Verificando se estamos na borda, porém do outro lado, caso sim, colocamos 0 em torno para possibilitar o calculo da mediana.
                    if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
                        temp.append(0)

                    else:
                        # Como foi confirmado que não estamos na borda, podemos fazer o calculo dos valores
                        # que estão dentro do filter_size, pegando o valor mediano dele.
                        for k in range(filter_size):
                            temp.append(data[i + z - indexer][j + k - indexer])

            temp.sort()
            # Recriamos o array que será convertido em imagem, utilizando os valores de mediana que salvamos no array temporario.
            data_final[i][j] = temp[len(temp) // 2]
            temp = []
    return data_final


def main():
    img = Image.open("../images/whitmore_noise.pgm")
    arr = numpy.array(img)
    removed_noise = median_filter(arr, 7)
    out = Image.fromarray(removed_noise)
    img.show()
    out.show()


main()