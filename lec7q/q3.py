marks1=int(input("enter 1st subject marks:"))
marks2=int(input("enter 2nd subject marks:"))
marks3=int(input("enter 3rd subject marks:"))

total_percentage=((marks1 +marks2+marks3)/300)*100

if(total_percentage>=40 ):
    print("u are pss")

else:
    print("u are fail")

marks1_percentage=(marks1/100)*100
marks2_percentage=(marks2/100)*100
marks3_percentage=(marks3/100)*100

if(marks1_percentage>=33):
    print("pass in this subject.")

else:
    print("u are fail in this subject")

if(marks2_percentage>=33):
    print("pass in this subject.")

else:
    print("u are fail")

    
if(marks3_percentage>=33):
    print("pass in this subject.")

else:
    print("u are fail")

    