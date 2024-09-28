lst = [1,2,3,4,5,6,3,4,5,7,6,5,4,3,4,5,4,3, 'Привіт', "анаконда"]
print("Лист до форматування ", lst)
temp_str_list = []
temp_int_list = []
def remove_duplicates(a):
    temp_list = []
    for i in a:
        if i not in temp_list:
            temp_list.append(i)
    return temp_list


def counting(lst_for_counting):
    for item in lst_for_counting:
        if type(item) == str:
            temp_str_list.append(item)
        elif type(item) == int:
            temp_int_list.append(item)
    return temp_int_list, temp_str_list


def sortsis(lst_str_for_sort, lst_int_for_sort):
    sorted = [item.lower() if type(item) == str else item for item in lst_str_for_sort]
    sorted.sort()
    lst_int_for_sort.sort()
    return lst_int_for_sort + sorted


temp_lst = remove_duplicates(a=lst)
temp_int_list, temp_str_list = counting(temp_lst)
sortt = sortsis(temp_str_list, temp_int_list)
print(sortt)

