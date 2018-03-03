# -*- coding: utf-8 -*-

def binary_search(numbers, number_to_find, low, high):
    if low > high:
        return False

    mid = (low + high) // 2

    if numbers[mid] == number_to_find:
        return True

    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid - 1)

    else:
        return binary_search(numbers, number_to_find, mid + 1, high)


if __name__ == '__main__':
    numbers = [3, 5, 6, 21, 22, 23, 28, 31, 34, 36, 39, 41, 44, 52, 56, 59, 66, 74, 90, 94]

    number_to_find = int(input('Ingresa un numero: '))

    result = binary_search(numbers, number_to_find, 0, len(numbers) - 1)

    if result is True:
        print('El numero si esta en la lista')
    else:
        print('El numero no esta en la lista')
