# using walrus operator 
if (n := len([1,2,3,4,5]))>6:
    print(f"list is too long({n}) element, expected <=3)")
else:
    print("")
