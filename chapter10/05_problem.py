from random import randint

class train:
    def __init__(self,trainno):
        self.trainno=trainno
        

    def book(self,fro,to):
        print(f"ticket is booked in train no:{self.trainno}from{fro}to{to}")
    
    def getstatus(self):
        print(f"this train  no {self.trainno}is running on tym")
      
    def getfare(self,fro,to):
        print(f"ticket fare in train no:{self.trainno}from{fro}to{to} is {randint(222,6666)}")
    
         
    
t=train(12395)
t.book("dhn","bhopal")
t.getstatus()
t.getfare("rampur","delhi")
    
