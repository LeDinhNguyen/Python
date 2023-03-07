month_dict = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if (year % 400 == 0) or (year  % 4 == 0 and year % 10 != 0):
    month_dict[2] = 29

print(month_dict[month])