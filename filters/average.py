import numpy
from PIL import Image


def average_filter(data, filter_size):
    temp = []
    indexer = filter_size // 2
    data_final = numpy.zeros((len(data),len(data[0])))
    for i in range(len(data)):

        for j in range(len(data[0])):

            for z in range(filter_size):
                # Verificando se estamos na borda, caso sim, colocamos 0 em torno para possibilitar o calculo da média.
                if i + z - indexer < 0 or i + z - indexer > len(data) - 1:
                    for c in range(filter_size):
                        temp.append(0)
                else:
                    # Verificando se estamos na borda, porém do outro lado, caso sim, colocamos 0 em torno para possibilitar o calculo da média.
                    if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
                        temp.append(0)

                    else:
                        # Como foi confirmado que não estamos na borda, podemos fazer o calculo dos valores
                        # que estão dentro do filter_size, pegando o valor mediano dele, e criando a
                        for k in range(filter_size):
                            temp.append(data[i + z - indexer][j + k - indexer])
            # Utilizamos a função average do numpy para calcular o valor médio dos valores do temp, que tem o mesmo tamanho do filter size
            data_final[i][j] = numpy.average(temp)
            temp = []
    return data_final


def main():
    img = Image.open("../images/whitmore_noise.pgm")
    arr = numpy.array(img)
    removed_noise = average_filter(arr, 7)
    out = Image.fromarray(removed_noise)
    img.show()
    out.show()


main()