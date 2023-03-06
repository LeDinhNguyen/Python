num = [1,2,3,4,5,6,7]

def findMaxOdd(num_list: list):
    max_odd = num_list[0]
    for num in num_list:
       if num % 2 != 0:
           if max_odd < num:
               max_odd = num

    return max_odd

print(findMaxOdd(num))
