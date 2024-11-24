X = int(input('Введите число: '))  # type: ignore
number_list = list(range(1, X+1))
#number_rev_list = number_list.reverse()
number_rev_list = list(reversed(number_list))
print(number_list)
print(number_rev_list)
