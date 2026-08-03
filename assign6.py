#1. create list of numbers from 1 to 20 using list comprehensation
# a=[ i for i in range(1,21)]
# print(a)


#2. list of even numbers between 1 to 50
# a=[ i for i in range(1,51) if i%2==0]
# print(a)


# #3. list of square of numbers from 1 to 10
# a=[ i**2 for i in range(1,11)]
# print(a)


#4. list of numbers>10
# num=[12,5,18,7,20,3]
# a=[ i for  i in num  if i>10]
# print(a)


#5. dictionary comprehensation
# a={ i:i**2 for i in range(1,6)}
# print(a)


#6. key and its length
# names=['anu','rahul','diya']
# length={i:len(i) for i in names}
# print(length)


#7. set of squares of numbers from 1 to 10
# a={ i:i**2 for i in range(1,11)}
# print(a)


#8. set containing first letter of each word
# words=['apple','banana','apple','orange','banana']
# a={ i:i[0] for i in words}
# print(a)


#9. 
# for i in range(5):
#     for j in range(5-i):
#         print('*',end=' ')
#     print()

# #10. 
# for i in range(4):
#     for k in range(i+1):
#         print(' ',end='')
#     for j in range(4-i):
#         print('*',end=' ')
#     print()                                


#11.
# for i in range(1,6):
#     for j in range(6-i):
#         print(' ', end=' ')
#     for k in range(i):
#         print('*', end=' ')
#     print()


#12.
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()


# #13.
# for i in range(6):
#     for k in range(6-i):
#         print('',end=' ')
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()


#14.




# #15.
# for i in range(6):
#     for j in range(1,i+1):
#         print(i,end=' ')
#     print()