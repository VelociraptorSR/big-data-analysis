main_string = input("enter any string ")
sub_string = input("enter a substring ")
counter = 0
l = len(sub_string)
lm = len(main_string)
for i in range(0,lm):
    if main_string[i:l+i] == sub_string:
        counter += 1
print(f"{sub_string} = {counter}")