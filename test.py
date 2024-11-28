X = int(input('Введите число: ')) 
number_list = list(range(1, X+1))
number_rev_list = list(reversed(number_list))
print(number_list)
number_dict = {}
for key in number_list:
    for value in number_rev_list:
        number_dict[key] = value
        number_rev_list.remove(value)
        break
print(number_dict)