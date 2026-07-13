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