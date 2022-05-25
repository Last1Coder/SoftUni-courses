# Task 04. Sum Of A Beach
input_line = str(input())
input_lower = input_line.lower()

br = 0
if "water" in input_lower:
    br += input_lower.count("water")
if "sand" in input_lower:
    br += input_lower.count("sand")
if "fish" in input_lower:
    br += input_lower.count("fish")
if "sun" in input_lower:
    br += input_lower.count("sun")
print(br)
