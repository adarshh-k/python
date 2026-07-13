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