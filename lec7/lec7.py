a=int(input("enter your age:"))

if(a>=18):
    print("you can vote")

elif(a<0):
    print("invalid age ,cannot be a negative age")

elif(a==0):
    print("age cant't be zero")

else:
    print("not applicable")   