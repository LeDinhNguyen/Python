numbers = list(map(int, input().split()))
maximum = 0

for num in numbers:
    if num > maximum:
        maximum = num

print(maximum)