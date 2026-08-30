name = input("enter any name ")
name_list = name.title().split(" ")
print(name_list)
new_list = []
for i in range(0,len(name_list)-1):
    short_name = name_list[i][0]+"."
    new_list.append(short_name)
new_list.append(name_list[-1])
print(" ".join(new_list))