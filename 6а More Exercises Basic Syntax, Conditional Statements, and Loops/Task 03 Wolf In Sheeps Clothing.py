# Task 03 Wolf In Sheeps Clothing
input_line = str(input())
input_list = input_line.split(", ")
# print(input_list)
if input_list[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    input_list.reverse()
    # print(input_list)
    for i in range(len(input_list)):
        if input_list[i] == "wolf":
            print(f"Oi! Sheep number {i}! You are about to be eaten by a wolf!")