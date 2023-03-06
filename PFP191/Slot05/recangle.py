vertical = int(input("Enter vertical: "))
horizontal = int(input("Enter horizontal: "))

if vertical <= 2 and horizontal <= 2:
    print("Error")

# hcn ko rong
for i in range(horizontal):
    for j in range(vertical):
        print("* ", end="")
    print()
print("\n")

# hcn rong
print("* "*vertical)

for i in range(horizontal - 2):
    print("* ", end="")
    for j in range(vertical - 2):
        print("  ", end="")
    print("* ", end="\n")

print("* "*vertical)
