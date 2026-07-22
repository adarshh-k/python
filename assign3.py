# #1. ask user how many elemts they want to enter
# li=[]
# n=int(input('How many elements u want to enter:'))
# for i in range(n):
#   e=input('Enter the elements:')
#   li.append(e)
# print(li)

# #2. add new item to list and display it
# items=["Messi","Neymar","ozil","pele"]
# newitems=input("Enter the new item to be added:")
# items.append(newitems)
# print("updated list",items) 

# #3. adding new color to position 
# li=["green","blue","yellow","red","purple"]
# position=int(input("Enter the position:"))
# newclr=input("Enter new color to be added:")
# li.insert(position,newclr)
# print(li)

# #4. combinening both list to sinle one
# li1=["samsung","redmi","motorola"]
# li2=["nothing","apple","realme"]
# li1.extend(li2)
# print(li1)

# #5. create a list of fruits
# fruits=["apple","mango","kiwi","orange","cherry"]
# n=input("Enter the fruit name givem:")
# if n in fruits:
#  fruits.remove(n)
#  print(fruits)
# else:
#  print("item not found")

#  #6. display the removed elemment and updated list
# li=[10,20,30,40,50]
# removed=li.pop()
# print("Removed elemet:",removed)
# print("updated list:",li)

# #7. studname exist or not
# studname=["akash","adarsh","abhi","yadhu","nandhu"]
# n=input("Enter the given student name:")
# if n in studname:
#     print("student name exist")
# else:
#     print("student name not exist!")

# #8. display count of elements
# li=["hey",'hello',"wow","hey",'nice',"hey"]
# n=input("enter the element:")
# count=li.count(n)
# print("count of element is:",count)

# # #9. 
# sub=["chemistry","physics",'biology',"maths","cs"]
# n=input("Enter any existing subject:")
# if n in sub:
#     index=sub.index(n)
#     new=input("Enter the new subject:")
#     sub[index]=new
#     print("updated list",sub)
# else:
#     print("subject  not found")

# #10. list of integers and reverse it
# int=[1,2,3,4,5,6,-3]
# int.reverse()
# print('Reversed list=',int)

# #11. display largest number in the list
# int=[1,2,3,4,5,6,]
# large = int[0]
# for i in int:
#     if i>large:
#         large=i
#         print("largest number=",large)

# #12. display smallest number 
# int=[2,3,4,5,6,]
# small = int[-1]
# for i in int:
#     if i<small:
#         small=i
#         print("smallest number=",small)

# #13. sum
# li=[1,2,3,4,5,6,]
# sum=sum(li)
# print("sum of all integers =",sum)

# #14. average
# li=[1,2,3,4,5]
# total=0
# for i in li:
#     total=total + i
#     average=total/len(li)
# print("avg=",average)

# #17. ascending descending
# li=[2,7,1,4,5,9,3]
# li.sort()
# print("ascending order:",li)
# li.sort(reverse=True)
# print("descending order:",li)

# #20. second largest
# int=[1,2,3,4,5,6,]
# seclarge = int[-2]
# for i in int:
#     if i>seclarge:
#         seclarge=i
#         print("second largest number=",seclarge)

#16. positive negative
li=[1,-2,3,5,-4,6]
positive = []
negative = []
for i in li:
    if i > 0:
        positive.append(i)
    else:
        negative.append(i)
        print("positive number",positive)
        print("negative",negative)