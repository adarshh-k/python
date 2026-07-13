a=int(input("Enter the age of first person:"))
b=int(input("Enter the age of second person:"))
c=int(input("Enter the age of third person:"))
d=int(input("Enter the age of fourth person:"))
if a<b and a<c and a<d:
    print("a is youngest person")
elif b<a and b<c and b<d:
    print("b is youngest person")
elif c<a and c<b and c<d:
    print("c is youngest person")
else:
    print("d is youngest person")