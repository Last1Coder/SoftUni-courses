# Task 01. Find The Largest
n = str(input())
n_list = [x for x in n]
# print(n_list)
n_list.sort(reverse=True)
# print(n_list)
n_str = "".join(n_list)
print(int(n_str))
