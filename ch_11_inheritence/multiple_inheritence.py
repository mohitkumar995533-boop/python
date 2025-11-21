class employee:
    company="itc"
    name="default name"
    def show(self):
        print(f"the name is{self.name} and the company is {self.company}")
        
        
class coder:
    language="python"
    def printLanguage(self):
        print(f"out pf all languages here is your language:{self.language}")
        
class programmer(employee,coder):
    company="itc infotech"
    def showlanguage(self):
        print(f"the name is {self.company} and he is good with {self.language}")
        
a = employee()
b= programmer()


b.show()
b.printLanguage()
b.showlanguage
        
        
    
     
     