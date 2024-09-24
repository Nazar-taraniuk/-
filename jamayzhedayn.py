a = [1,2,3,4,5,6,3,4,5,7,6,5,4,3,4,5,4,3, 'Привіт', "анаконда"]
print("Лист до форматування ", a)
temp_list = []
temp_str_list = []
temp_int_list = []
k = set()
def remove_duplicates(a):
    for i in a:
        if i not in k:
            temp_list.append(i)
            k.add(i)


remove_duplicates(a)

def counting():
    for item in k:
        if type(item) == str:
            temp_str_list.append(item)
        elif type(item) == int:
            temp_int_list.append(item)



counting()

new_lst = [item.lower() if type(item) == str else item for item in temp_str_list]

def sortsis():
    new_lst.sort()
    return temp_int_list + new_lst

u = sortsis()
print(u)