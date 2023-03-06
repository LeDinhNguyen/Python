string = input("Enter string: ")
count_digit = 0
count_special = 0
for s in string:
    if s.isdigit():
        count_digit += 1
    else:
        count_special += 1

print(count_digit)
print(count_special)