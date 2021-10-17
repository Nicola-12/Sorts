def merge_sort(array):

    if len(array) > 1:

        meio = len(array)//2

        left_array = array[:meio]
        right_array = array[meio:]

        merge_sort(left_array)
        merge_sort(right_array)

        i = 0
        j = 0
        k = 0

        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1

            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1

    return array


def integer_list(string_list):
    integer_map = map(int, string_list)
    return list(integer_map)
    
def string_list(integer_list):
    return ''.join(map(str, integer_list))


with open('sorted.txt', 'w') as outfile:
    with open('partial-1.txt', 'r') as file1:
        with open('partial-2.txt', 'r') as file2:
            list1 = file1.readlines()
            list2 = file2.readlines()
            for i in range(len(list1)):
                minimo = min(integer_list(list1[i].split()), integer_list(list2[i].split()))
                outfile.write(string_list(merge_sort(minimo)))
                outfile.write("\n")
