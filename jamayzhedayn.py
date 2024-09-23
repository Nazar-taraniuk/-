a = [1,2,3,4,5,6,3,4,5,7,6,5,4,3,4,5,4,3, 'Привіт', "анаконда"]
print("List Before ", a)
temp_list = []
temp_str_list = []
temp_int_list = []
for i in a:
    if i not in temp_list:
        temp_list.append(i)

a = temp_list
print("List After removing duplicates ", a)

a = list(set(a))

for item in a:
    if type(item) == str:
        temp_str_list.append(item)
    elif type(item) == int:
        temp_int_list.append(item)


new_lst = [item.lower() if type(item) == str else item for item in a]
print(new_lst)