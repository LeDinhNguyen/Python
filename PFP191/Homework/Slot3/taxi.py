distance = float(input("Enter a distance (km): "))
money = 0
vnd = 1000
# count money
if distance < 1:
    money = money * 15
elif distance >= 1:
    money = 15 + (distance - 1) * 13.5
elif distance >= 5:
    money = 15 + 4*13.5 + (distance - 5) * 11

# discount
if distance > 120:
    money = money * 0.9

print(money*vnd)