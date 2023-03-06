"""
Perfect number is the number that is equal to the sum of its all divisors (not included the largest divisor)
1. Find sum of all divisors
2. Check that the sum is equal to the given number
"""
number = int(input("Enter the number: "))
sum_of_divisors = 0

# find sum of
for divisor in range(1, number):
    if number % divisor == 0: # check if it is divisor
        sum_of_divisors += divisor # sum of all divisors

# check perfect number
if number == sum_of_divisors:
    print("Perfect Number")