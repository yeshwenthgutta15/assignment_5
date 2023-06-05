class python:

 # constructor

     def __init__(self):             
         self.p = 0
         self.a = 0
          # instance method

     def getinput(self):                            
         self.p = int(input('Enter p:   '))
         self.a = int(input('Enter a:   '))
         self.c = int(input('Enter c:   '))

     def sqsum(self):
         return (self.p * self.p) + (self.a * self.a) + (self.c * self.c)
      # calling construtor

obj = python()                      
obj.getinput()
res = obj.sqsum()
print("Squared values : ",res)