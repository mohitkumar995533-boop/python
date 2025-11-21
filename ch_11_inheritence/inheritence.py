class employee:
    company="itc"
    def show(self):
     print(f"the name is{self.name} and the salary is {self.salary}")
    
# class programmer:
    # company= "itc infitech"
    # def show(self):
        # print(f"the name is{self.name} and the salary is {self.salary}")
        
    # def showlangauge(self):
        # print(f"the name is {self.name} and the salary is{self.salary}")
        
class programmer(employee):
    company="itc infotech"
    def showlanguage(self):
        print(f"the name is {self.name} and the salary is {self.salary}")
            
a=employee()
b=programmer()

print(a.company, b.company) 