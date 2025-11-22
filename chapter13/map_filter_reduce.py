from functools import reduce 
l = [2,4,6,7,5]

square = lambda x: x*x


sqlist = map(square,l)
print(list(sqlist))


#map list ke andar function chalane m help krta




#filter example

def even(n):
    if(n%2==0):
        return True
    return False

onlyeven = filter(even,l)
print(list(onlyeven))
# onlyodd = filter(odd,l)
# print(list(onlyodd))



#reduce example


def sum (a,b):
    return a+b
print(reduce(sum,l))
