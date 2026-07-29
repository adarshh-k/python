# #1. print numbers from 1 to 50 in reverse
# for i in range(50,0,-1):
#   print(i)  


#   #2. even numbers from 1 to 100
# for i in range(1,101):
#     if i%2==0:
#      print(i)  


# #3. odd numbers from 1 to 100
# for i in range(1,101):
#     if i%2!=0:
#        print(i)  


# 4. #divisible by 7 in between 1 and 100
# for i in range(1,100):
#     if i%7==0:
#      print(i)  


# #6. # #sum of first N natural numbers
# n=int(input("Enter the number:"))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)


# #7. product of first N natural numbers
# n=int(input("Enter a number:"))
# pdt=1
# for i in range(1,n+1):
#     pdt*=i
# print(pdt)


# #8. count of numbers from 1 to 100 divisible by 3
# count=0
# for i in range(1,101):
#  if i%3==0:
#     count+=1
# print(count)


# #9. summ of all even numbers from 1 to 100
# sum=0
# for i in range(2,101,2):
#      sum+=i
# print(sum)


# #10. count of upper and lowercase count from a string
# a=input("Enter a string:")
# uppercount=0
# lowercount=0
# for i in a:
#     if i.isupper():
#         uppercount+=1
#     else:
#      if i.islower():
#         lowercount+=1
# print("uppercount=",uppercount)
# print("lowercount=",lowercount)


#11. 
# a=input("Enter a string:")


#12. 
li=[1,2,3,4,8]
largest=li[0]
seclarge=li[0]
for i in li:
    if i>largest:
        seclarge=largest
        largest=i
    elif i>seclarge and i!=largest:
        seclarge=i
        print(seclarge)


# #13. duplicate 
# a=[2,3,4,5,4,6,3,2]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print("unique list=",b)


# #14. count of numbers divided by 3 and 5
# t=(10,15,20,30,33)
# count=0
# for i in t:
#     if i%3==0 and i%5==0:
#         count+=1
# print('count of num div by 5 and 3:',count)


# #15. dictionary
# student={
#     'adhruu':80,
#     'akshara':19,
#     'akash':44,
#     'sree':67,
#     'dhyan':98
# }
# # print("studentmark:",student)
# topper= student.keys[0]
# for i in student.values():
#     if i>topper:
#         topper=i
#         print(topper)


# #17. difference between 2 sets
# a={'a','b','c','e'}
# b={'a','b','d','f'}
# a.symmetric_difference_update(b)
# print(a)


# #22. list of integers
# li=[0,1,4,5,6,8,9]
# sum=0
# for i in li:
#     if i%2==0 and i%4!=0:
#         sum+=i
# print('sum of numbers:',sum)


# #19. list of integers in odd and even
# li=[1,2,3,4,7,8,9]
# evencount=0
# oddcount=0
# for i in li:
#     if i%2==0:
#      evencount+=1
#     else:
#      oddcount+=1
# print("Evencount=",evencount)
# print('oddcount=',oddcount)


# #21. tuple with larger value at each position
# t1=(1,2,3,4,10)
# t2=(4,5,6,4,3)
# a=len(t1)
# for i in range(a):
#     if t1[i]>t2[i]:
#         print('t1 is greatest')
#     elif t1[i]<t2[i]:
#         print('t2 is greatest')
#     else:
#         print('equal')