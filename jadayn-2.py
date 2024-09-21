mark = "hello world"
print (mark)
print (type(mark))
name = "Назар"
second_name = "Таранюк"
print (name, second_name)
print (type(name))
age = 16
print(age)
print (type (age))

count_int = 0
count_str = 0
count_float = 0
count_set = 0
count_tuple = 0
count_bool = 0
count_list = 0
count_notnull = []
max_value = 0
lst_notnull = []
lst_count_types = [count_list, count_bool, count_set, count_float, count_tuple, count_str, count_int]
lst = [name, second_name, age]
lst_name_type = [int, str, str, int, str, str]
for item in lst:
    if type(item) == int:
        lst_count_types[-1] +=1
    elif type(item) == str:
        lst_count_types[-2] +=1
    elif type(item) == tuple:
        lst_count_types[-3] +=1
    elif type(item) == float:
        lst_count_types[-4] +=1
    elif type(item) == set:
        lst_count_types[-5] +=1
    elif type(item) == bool:
        lst_count_types[-6] +=1
    elif type(item) == list:
        lst_count_types[-7] +=1
for item in lst_count_types:
    if item !=0:
        lst_notnull.append(item)
    if len(lst_notnull) == 1:
        print('Good')
    else:
        if item > max_value:
            max_value = item

max_value = max(lst_count_types)
inn = lst_count_types.index(max_value)
print(lst_name_type[inn])
for item in lst:
    if type(item) !=lst_name_type[inn]:
        lst.remove(item)