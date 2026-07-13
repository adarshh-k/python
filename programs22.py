# 1. print hello if no is 10
num=int(input("enter a number="))
if num == 10:
 print("Helloo") 
else:
  print(num)

#2. check no is positive
  num=int(input("Enter a numbers:"))
if num>=0:
 print("Entered number is positive")
else:
 print("Entered number is not positive")

#3. check no is between 1 and 10
num=int(input("Enter a number="))
if num>0 and num<11:
    print("Entered number is in between 1 and 10")
else:
    print("Entered number is not in between 1 and 10")

#4. ckeck if vowel
char=input("Enter a character: ")
if char in ['a','e','i','o','u']:
  print("character is a vowel")
else:
  print("character is not a vowel")

#5. find largest among 2 nos
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if (num1>num2):
  print("num1 is larger than num2")
elif (num2>num1):
  print("num2 is greater than num1")

#6. find smallest among 2 nos
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if (num1<num2):
  print("num1 is smaller than num2")
elif (num2<num1):
  print("num2 is smaller than num1")

#7. eligible for voting
age=int(input("Enter age:"))
if age>= 18:
    print("Eligible for voting")
else:
    print("Not eligible for voting!")

#8. check no is odd or even
num=int(input("Enter a number:"))
if num % 2==0:
    print("Given number is even")
else:
     print("Given number is odd")

#9. check no is divisible by 3
num=int(input("Enter a number:"))
if num % 3==0:
    print("Divisible by 3")
else:
     print("Not divisible by 3")

#10. check no is divisible by both 2 and3
num=int(input("Enter a number:"))
if num % 2==0 and num % 3==0:
    print("Divisible by both 2 and 3")
else:
     print("Not divisible by 2 and 3")

#11. check no is positive,negative or zero
num=int(input("Enter a numbers:"))
if num>0:
 print("Entered number is positive")
elif num<0:
 print("Entered number is negative")
else:
  print("Number is zero")

#12. percentage and grade
mark=int(input("Enter your mark:"))
if mark>=81 and mark<=100:
    print("Grade=A+")
elif mark>=71 and mark<=80:
    print("Grade=A")
elif mark>=61 and mark<=70:
    print("Grade=B+")
elif mark>=51 and mark<=60:
    print("Grade=B")
elif mark>=41 and mark<=50:
    print("Grade=C")
elif mark>=31 and mark<=40:
    print("Grade=D")
else:
    print("Failed")

#13. largest among 3 nos
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a>b and a>c:
    print(a, "is largest number")
elif b>a and b>c:
    print(b, "is largest number")
else:
    print(c, "is largest")

#14. age of 4 people and display youngest
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

#15. cost of bike and road tax
cost=int(input("Enter the cost of bike:"))
if cost>100000:
    print("Tax=15%")
elif cost>50000 and cost<=100000:
    print("Tax=10%")
else:
    print("Tax=5%")

#16. employee bonus based on year of service
salary=float(input("Enter salary:"))
service=int(input("Enter years of services:"))
if service > 10:
    bonus = salary * 10 / 100
    print("bonus= ", bonus)
elif service >=6 and service <= 10:
     bonus = salary * 8 / 100
     print("bonus=", bonus)
else:
     bonus = salary * 5 / 100
     print("bonus=", bonus)

#17. Hello if no is multiple of 5 otherwise Bye
num=int(input("enter a number="))
if num %5 == 0:
    print("Hello")
else:
    print("Bye")

#18. check lat no is divisible by 3
num=int(input("Enter a number="))
last_digit = num % 10
if last_digit % 3 == 0:
   print("Last digit is divisible by 3")
else:
   print("Last digit is not divisible by 3")

#19. performing operation
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
operator=input("Enter operator(+,-,*,/):")
if operator == "+" :
   print(a+b)
elif operator == "-" :
    print(a-b)
elif operator == "*" :
     print(a*b)
elif operator == "/" :
     print(a/b)
else:
    print("invalid operator")

#20. calcukating wage
age=int(input("Enter age="))
gender=(input("Enter gender(male/female)="))
wday=int(input("Enter the no.of working days="))
if age>=18 and age<=29:
    if gender == "male":
        wage = 700 * wday
        print("Total wage is= " ,wage)
    elif gender == "female":
        wage = 750 * wday
        print("Total wage is=" , wage)
elif age>=30 and age<=40:
    if gender == "male":
        wage = 800 * wday
        print("Total wage is=" , wage)
    elif gender == "female":
        wage = 850 * wday
        print("Total wage=",wage)
else:
       print("Not applicable")

#21. calculating wages using nested if
age=int(input("Enter age="))
gender=(input("Enter gender(male/female)="))
wday=int(input("Enter the no.of working days="))
if age>=18 and age<=29:
    if gender == "male":
        wage = 700 * wday
        print("Total wage is=" ,wage)
    elif gender == "female":
        wage = 750 * wday
        print("Total wage is=", wage)
elif age>=30 and age<=40:
    if gender == "male":
        wage = 800 * wday
        print("Total wage is=", wage)
    elif gender == "female":
        wage = 850 * wday
        print("Total wage=",wage)
else:
     print("Enter age between 18 and 40")

#22. place of service using nested if
age=int(input("Enter age="))
gender=(input("Enter gender(male/female)="))
status=(input("Enter status(married/unmarried)="))
if age>=20 and age<=39:
 if gender == "male":
    print("Employee works anywhere")
elif age>=40 and age<=60:
    print("Employee works in urban area")
elif gender== "female":
    print("Employee works in urban area")
else:
    print("Error")