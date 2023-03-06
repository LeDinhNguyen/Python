def lucasList(a: int, b: int, n: int) -> list:
    if n < 1:
        return []
    elif n == 1:
        return [a]
    else:
        lucas = [a, b]
    i = 2
    while len(lucas) < n:
        lucas.append(lucas[-1] + lucas[-2])
        i += 1
    return lucas

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
n = int(input("Enter number: "))
print(lucasList(a, b, n))

