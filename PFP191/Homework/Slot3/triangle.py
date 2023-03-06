a = int(input())
b = int(input())
c = int(input())

triangle_condition = (a + b > c) and (b + c > a) and (c + a > b)

if triangle_condition:
    print("YES")
else:
    print("NO")