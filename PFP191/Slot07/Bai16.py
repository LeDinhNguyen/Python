def sum1toN(n: int) -> float:
    if n == 1:
        return 1
    return (n * (n + 1)) / 2


def S(x, n):
    count = 0
    for i in range(1, n + 1):
        count += (x**i) / (sum1toN(i))

    return count


# x = int(input("Enter number x = "))
# n = int(input("Enter number n = "))

x, n = map(int, input().split())
print(S(x, n))
