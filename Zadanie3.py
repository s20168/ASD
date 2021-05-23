# set_of_numbers = [0, 1, 1, 0, 1, 0, 1]
set_of_numbers = [4, 14, 14, 4, 14, 4, 14]
for i in range(len(set_of_numbers) - 1, -1, -1):
    temporary_index = 0
    for j in range(0, i + 1, 1):
        if set_of_numbers[j] > set_of_numbers[temporary_index]:
            temporary_index = j
    temporary_list = set_of_numbers[i]
    set_of_numbers[i] = set_of_numbers[temporary_index]
    set_of_numbers[temporary_index] = temporary_list
print('Sorted list is: ', set_of_numbers)