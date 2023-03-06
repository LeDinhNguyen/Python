def ruleS(number: int) -> float:
    mau = 6
    if number % 2 != 0:
        return False
    while number >= 4:
        print(mau)
        mau = (number - 2) + (number - 1) / mau
        number -= 2
        print(number)

    return 1 / mau


def main():
    print("Chuong trinh tinh tong theo cong thuc")
    num = int(input("Enter n = "))
    print(ruleS(num))
    print("Cam on ban da su dung chuong trinh")


if __name__ == "__main__":
    main()
