lst = [1,2,3,4,5,6,3,4,5,7,6,5,4,3,4,5,4,3, 'Привіт', "анаконда"]
print("Лист до форматування ", lst)
temp_str_list = []
temp_int_list = []
k = set()
def remove_duplicates(a):
    temp_list = []
    for i in a:
        if i not in k:
            temp_list.append(i)
            k.add(i)
    return temp_list


def counting(lst_for_counting):
    for item in lst_for_counting:
        if type(item) == str:
            temp_str_list.append(item)
        elif type(item) == int:
            temp_int_list.append(item)
    return temp_int_list, temp_str_list


def sortsis(lst_for_sort):
    sorted = [item.lower() if type(item) == str else item for item in lst_for_sort]
    sorted.sort()
    return temp_int_list + sorted


temp_lst = remove_duplicates(a=lst)
lst_for_counting, lst_for_dayn = counting(temp_lst)
u = sortsis(lst_for_dayn)
print(u)
