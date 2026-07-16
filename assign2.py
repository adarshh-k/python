# #1. Length of the string
# a=input("Enter a string:")
# print("length of the string=",len(a))


# #2. Print each char in new line
# a=input("Enter a string:")
# for i in a:
#     print(i)


# #3. string concatination
# a=input("Enter a string1:")
# b=input("Enter a string2:")
# c= "".join([a,b])
# print(c)


# #4. reverse string
# a=input("Enter a string:")
# print(a[::-1])


# #5. uppercase
# a=input("Enter a string:")
# b=a.upper()
# print(b)


# #6. lowercase
# a=input("Enter a string:")
# b=a.lower()
# print(b)


# #7. check string contains only digits
# a=input("Enter a string=")
# print(a.isnumeric())


# #8. counting no.of spaces in a string
# a=input("Enter a string=")
# print(a.count(' '))


# #9. removeing spaces
# a=input("Enter a string=")
# b=a.replace(" ","")
# print(b)


# #10. replace occurance of a string
# a=input("Enter a string=")
# b=input("Enter the character to replaced=")
# c=input("Enter new character=")
# d=a.replace(b,c)
# print(d)


# #11. counting vowels
# a=input("Enter a string=")
# vow=['a','e','i','o','u']
# count=0
# for i in a:
#     if i in vow:
#         count+=1
# print(count)


# #12. counting no.of upper and lower case
# a=input("Enter a string=")
# upper_count=0
# lower_count=0
# for i in a:
#     if i.isupper():
#         upper_count+=1
#     else:
#         lower_count+=1
# print("uppercount=",upper_count)
# print("lowercount",lower_count)


# #13. finding first occurance of a string
# a=input("Enter a string=")
# print(a.index('a'))

# #14. finding  last occurance of a string
# a=input("Enter a string=")
# print(a).')
       

# #15. checking string starts with vowel
# a=input("Enter a string=")
# if a[0] in ['a','A','e','E','i','I','o','O','u','U']:
#     print("String starts with vowel")
# else:
#     print("string does not starts with vowel")


# #16. check if string is paliandrome
# a=input("Enter a string=")
# if a== a[::-1]:
#     print("string is palindrome")
# else:
#     print("not a palindrome")


# #17. counting no.of words in string
# a=input("Enter a string=")
# count=0
# for i in a:
#     count=count+1
#     print(count)


# #18. remove duplicate characters in string
# a=input("enter the string=")
dup=" "
  

# #19. count total no.of digits and characters
# a=input("Enter the string=")
# isalpha_count=0
# isnumeric_count=0
# for i in a:
#     if i.isalpha():
#         isalpha_count+=1
#     else:
#         isnumeric_count+=1
# print("no.of digits",isalpha_count)
# print("no.of characters",isnumeric_count)
