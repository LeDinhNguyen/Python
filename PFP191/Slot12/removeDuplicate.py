def removeDuplicate(num_list: list) -> list:
    b = []
    for num in num_list:
        if num not in b:
            b.append(num)

    return b

a = [1,1,2,3,4,5,1,2,4,3]
print(removeDuplicate(a))