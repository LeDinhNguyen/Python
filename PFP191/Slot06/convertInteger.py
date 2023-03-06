num = int(input("Enter number: "))
convert_num = 0

while num > 0:
    lastDigit = num % 10
    convert_num = convert_num * 10 + lastDigit

    i += 1
    num = num // 10

print(convert_num + 1)
