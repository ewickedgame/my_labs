///////////////задача1/////////////
any_list = [1,2,3,4,5,6,7,8,9,10]
result = []
def odd_index(list):
    for i in range(len(list)):
        if i % 2 == 0:
            result.append(list[i])
    print(result)
odd_index(any_list)

///////////////задача2/////////////
any_list = [1,2,3,4,5,6,7,8,9,10]
result = []
def more(list):
    for i in range(len(list)):
        if list[i] > list[i - 1]:
            result.append(list[i])
    print(result)
more(any_list)

///////////////задача3/////////////
any_list = [1,2,3,4,5,6,7,8,9,10]
def replacement(list):
    i_of_max_el = list.index(max(list))
    i_of_min_el = list.index(min(list))
    list[i_of_max_el], list[i_of_min_el] = list[i_of_min_el], list[i_of_max_el]
    print(list)
replacement(any_list)

///////////////задача4/////////////
d = {1: ':с', 2: 'Адам Смит', 3: 'Вторник'}
key = int(input('Введите ключ, чтобы получить его значение: '))
def get_value(dictionary):
    value = dictionary.get(key)
    print(value)
get_value(d)

///////////////задача5/////////////
from figures import triangle_area
triangle_area()
