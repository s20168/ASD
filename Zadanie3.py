# set_of_numbers = [0, 1, 1, 0, 1, 0, 1]
set_of_numbers = [4, 14, 14, 4, 14, 4, 14]
for i in range(len(set_of_numbers) - 1, -1, -1):
    index = 0
    for j in range(0, i + 1, 1):
        if set_of_numbers[j] > set_of_numbers[index]:
            temporary_index = j
    list = set_of_numbers[i]
    set_of_numbers[i] = set_of_numbers[index]
    set_of_numbers[index] = list
print('Sorted list is: ', set_of_numbers)