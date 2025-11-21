class employee:
    language="py"
    salary=15000
    
    def __init__(self,name,salary,language):
        print("i am creating an object")
        
        self.name= name
        self.salary=salary
        self.language=language
        
    def getinfo(self):
        print(f"the language is{self.language}.the salary is {self.salary}")
        
        
    @staticmethod
    def greet():
        print("good morning")
        
rohit=employee("rohit",1200,"java")
print(rohit.name,rohit.salary ,rohit.language)