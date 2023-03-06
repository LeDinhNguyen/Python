def getTotalX(a, b):
    # Write your code here
    a_multiply = []
    result = []

    for num in range(max(a), min(b) + 1):
        count = 0
        for j in range(len(a)):
            if num % a[j] == 0:
                count += 1
            print("count:", count)

        if count == len(a):
            a_multiply.append(num)
        print(num, a_multiply)

    print(a_multiply)
    # find fractor of list b from the result list
    for i in range(len(a_multiply)):
        count = 0
        for j in range(len(b)):
            print("b:", b[j], end=" ")
            print("mul:", a_multiply[i])
            if b[j] % a_multiply[i] == 0:
                count += 1

        if count == len(b):
            result.append(a_multiply[i])
        print(result)
    return len(result)
