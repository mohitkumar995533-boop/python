class employee:
    language="py"
    salary=15000
    
    def getinfo(self):
        print(f"the language is{self.language}.the salary is {self.salary}")
        
        
    @staticmethod
    def greet():
        print("good morning")
        
        
mohit=employee()
print(mohit.salary, mohit.language)
mohit.greet()
mohit.getinfo()



    
    
