a = int(input())
b = int(input())
c = int(input())

# a*x2 + b*x + c = 0

if a == 0:
    if b == 0:
        if c == 0:
            print("PT vo so nghiem")
        else:
            print("Pt vo nghiem")
    else:
        x = - c / b
else:
    delta = b*b - 4*a*c
    if delta < 0:
        print("PT vo nghiem")
    elif delta == 0:
        print("Nghiem la: ")
    else:
        print("Nghiem la: ")
