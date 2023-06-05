class calculator:
    def getinput(self):
        n1 = int(input('Enter no1:   '))
        n2 = int(input('Enter no2:   '))
        return n1, n2

    def add_it(self,num1, num2):
        return num1 + num2
    def subtract_it(self,num1, num2):
        return num1 - num2
    def multiplication_it(self,num1, num2):
        return num1 * num2
    def divison_it(self,num1, num2):
        return num1 / num2
    
    
obj = calculator()
num1, num2 = obj.getinput()
result = obj.add_it(num1, num2)
print("Addition: ",result)
result = obj.subtract_it(num1, num2)
print("subtraction: ",result)
result = obj.multiplication_it(num1, num2)
print("Multiplication: ",result)
result = obj.divison_it(num1, num2)
print("Divison: ",result)