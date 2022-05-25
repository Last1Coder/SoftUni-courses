# Task 02. Find The Capitals
input_line = str(input())
# input_list = [x for x in input_line if 65 <= ord(x) <= 90]
input_list = list()
for i in range(len(input_line)):
    if 65 <= ord(input_line[i]) <= 90:
        input_list.append(i)
print(input_list)
