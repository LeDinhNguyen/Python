"""
n = 5 number of people
k = 200 maximum weigh of a boat
list = [30, 80, 100, 150, 200]
coutn = 0




"""

# n = int(input("Enter the total of people: "))
# k = int(input("Enter the maximum weight in one boat: "))
# list_of_people = list(map(int, input().split()))
# count = 0

n = 5
k = 200
people = [30, 80, 100, 150, 200]
count = 0

# pointer
left = 0
right = n - 1

while left < n and right >= 0 and left < right:
	if people[left] + people[right] > 200: 
		count += 1
		right -= 1
	else:
		count += 1
		right -= 1
		left += 1

print(count)

