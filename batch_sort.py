def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        # recursivamente na sublista à esquerda (menores)
        quicksort(lista, inicio, p-1)
        # recursivamente na sublista à direita (maiores)
        quicksort(lista, p+1, fim)


def partition(lista, inicio, fim):
    # o pivo pode ser qualquer número da lista. Nesse caso, escolhemos para ser sempre o último
    pivot = lista[fim]
    i = inicio
    # looping que percorre toda a lista, onde o j representa o elemento em análise
    for j in range(inicio, fim):
        # j também serve para delimitar os elementos maiores que o pivô
        if int(lista[j]) <= int(pivot):
            # se j for menor que o pivot, ele troca de lugar com o primeiro elemento da lista dos maiores
            lista[j], lista[i] = lista[i], lista[j]
            # incrementa-se o limite dos elementos menores que o pivô
            i = i + 1
    # após o looping, o pivot (último elemento) vai para o seu lugar correto
    lista[i], lista[fim] = lista[fim], lista[i]
    return i


def split(word):
    return list(word)


def integer_list(string_list):
    integer_map = map(int, string_list)
    return list(integer_map)


def string_list(integer_list):
    return ''.join(map(str, integer_list))


file1_path = './numbers-1.txt'
file2_path = './numbers-2.txt'

outfile1_path = './partial-1.txt'
outfile2_path = './partial-2.txt'


def write_files(file_path, outfile_path):
    int_list = []
    new_lines = []

    with open(file_path, 'r') as file:
        content = file.readlines()
        for line in content:
            word = line.split()
            for i in word:
                new_list = split(i)
                int_list = integer_list(new_list)
                quicksort(int_list)
                new_lines.append(string_list(int_list))

    outfile = open(outfile_path, "w")
    new_lines.sort()
    for line in new_lines:
        outfile.writelines(line)
        outfile.writelines("\n")

    file.close()
    outfile.close()


write_files(file1_path, outfile1_path)
write_files(file2_path, outfile2_path)
