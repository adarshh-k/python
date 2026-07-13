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
