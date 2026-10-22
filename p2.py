class employee:
    def __init__(self,name,occ):
        # print("hey, iam a software dovelpoer")
        self.name=name
        self.occ=occ

    def info(self):
        print(f"{self.name} is a {self.occ}.")


    

a=employee("chandan","software doveloper")
b=employee("chandu","HR")

a.info()
b.info()

