class student:
    name = "chandan"
    course = "BCA"
    fee = 100000
    college = "indian acadamy "
    def info(self):
        print(f"{self.name} is a {self.course} studing at {self.college}.")


a=student()
b=student()
c=student()
a.name="vijay"
a.college="indian acadamy degree college"

b.name="chandu"
b.course="B.com"
b.college="indian acadamy degree college"

a.info()
b.info()
c.info()

