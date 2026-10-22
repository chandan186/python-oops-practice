class person:
    name = "chandan"
    occupation = "software doveloper"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=person()
b=person()
c=person()
d=person()
a.name="vijay"
a.occupation="accountant"

b.name="chandana"
b.occupation="HR"

# print(a.name)
# print(a.occupation)
a.info()
b.info()
c.info()
d.info()