def isPrime(number: int):
    count = 0
    for i in range(2, number // 2):
        if number % i == 0:
            count += 1

    return count == 0


def main():
    list_of_prices = []
    gift = 0
    total = 0
    found = False

    print("Chuong trinh tinh tien hoa don")
    while not found:
        number = int(
            input(
                "Enter the price of the product (press -1 for stopping the program): "
            )
        )
        if number > 0:
            list_of_prices.append(number)
        else:
            found = True

    if len(list_of_prices) > 0:
        # find the special gift
        for price in list_of_prices:
            if isPrime(price) and price >= 100 and price <= 999 and price > gift:
                gift = price

        # count total of the mount of money that the customer have to pay
        for price in list_of_prices:
            if price >= 100:
                if price == gift:
                    total += 0
                else:
                    total += price * 0.5
            else:
                total += price

        print("Tong so tien sau giam gia: ", int(total))
        print("San pham duoc tang qua la: ", gift)


if __name__ == "__main__":
    main()
