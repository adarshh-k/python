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