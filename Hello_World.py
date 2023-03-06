print("Hello World!")

class Student():
    def __init__(self, name, age):
        self.ten = name
        self.tuoi = age
    def study(self):
        print("Dang hoc")

bom = Student("Nguyen", 17)

print(bom.ten)
print(bom.study())
