class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def add(self):
        print("The addition of two numbers",self.a+self.b)
    
    def sub(self):
        print("The subtraction of two numbers",self.a-self.b)

a,b=map(int,input("Enter the two numbers: ").split())
calc=calculator(a,b)
calc.add()

