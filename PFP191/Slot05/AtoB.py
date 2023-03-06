A = int(input("Enter number A: "))
B = int(input("Enter number B: "))
sum_odd = 0

if A > B:
    start = B
    end = A
else:
    start = A
    end = B

for i in range(start, end + 1):
    if i % 2 != 0:
        sum_odd += i

print(sum_odd)