class colour:
    def __init__(self,w,b):
        self.colour1=w
        self.colour2=b

    def info(self):
        print(f"{self.colour1} and {self.colour2} both suits on you .")

a=colour("white","black")

a.info()