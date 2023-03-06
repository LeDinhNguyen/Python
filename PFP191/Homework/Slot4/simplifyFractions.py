"""
numerator > 0
denominator < 0
---------------
==> numerator < 0
    denominator > 0
and
numerator < 0
denominator < 0
---------------
==> numerator < 0
    denominator > 0

"""

numerator = int(input("Enter numerator: "))
denominator = int(input("Enter denominator: "))
maximum = max(abs(numerator), abs(denominator))

if denominator < 0:
    denominator = -denominator
    numerator = -numerator

for i in range(1, maximum + 1):
    if (numerator % i == 0) and (denominator % i == 0):
        numerator = int(numerator / i)
        denominator = int(denominator / i)
    print(numerator, denominator)
