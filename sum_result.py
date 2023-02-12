
def sum_result():

    while True:
        try:
            first_term = input('Введите певое слагаемое: ')
            first_term = float(first_term)
            break
        except ValueError:
            print('\n\nВы ввели некоректные данные для первого значения!\n  !!! Используйте только цифры и числа !!!')
            continue

    while True:
        try:
            second_term = input('Введите второе слагаемое: ')
            second_term = float(second_term)
            break
        except ValueError:
            print('Вы ввели некоректные данные для второго значения!\n  !!! Используйте только цифры и числа !!!')
            continue
    return print(f'{first_term} + {second_term} = {first_term + second_term}')


if __name__ == '__main__':
    sum_result()
