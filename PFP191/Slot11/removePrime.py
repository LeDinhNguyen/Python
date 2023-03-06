def isPrime(num):
    count = 0
    if num == 0 or num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                count += 1
    return count == 0
def removePrime(num_list: list):
    i = 0
    while i < len(num_list):
        print()
        if isPrime(num_list[i]):
            num_list.pop(i)
        i += 1
    return num_list

num_list = [1,2,3,4,5,6,7,7,8,9,10]
print(removePrime(num_list))