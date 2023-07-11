# 1. Split the file name and extensions
# import os
# file=input("enter the file name and extension:")
# filename,fileextension=os.path.splitext(file)
# print("the file name is:" +filename)
# print("the file extension is:" +fileextension)
# 1.1
# if fileextension==".mp3":
#     print("this fie is not allowed")

# 2. fahrenheit to centrigrade and kelvin
# f=float(input("enter the fahrenheit: "))
# ftoc=(f-32)*(5/9)
# print(ftoc)
# ftok=ftoc+273.15
# print(ftok)
# 2.1
# celisus=float(input("enter the celisus: "))
# ctof=(celisus*1.8)+32
# print("the celisus to fahrenheit %.2f" % (ctof))
# k = celisus + 273.15
# print("the celisus to kelvin",round(k,2))

# 3.calculate circumference of the circle and area of the circle
# import math
# r=int(input("enter the radius :"))
# c=2*math.pi*r
# # circumference of a circle =2*pi*r
# print("circumference of a circle",c)
# a=2*math.pi*r*r
# # area of circle =2*pi*r*r
# print("area of a circle",a)
#
# 3.1 half the circumference and area of the circle add them both and display result
# result=0.5*(c+a)
# print("result of the circumference and area of circle half value is ",result)

# 4 to get pwd
# check alpha num,
# char more 8 and less than 20
# pwd = input("Enter your password")# 3483803
#
# if(pwd.isalnum() and not pwd.isalpha() and not pwd.isdigit()):
#     if(len(pwd) > 8 and len(pwd) < 20):
#         print("Your password is okay")
#     else:
#         print("Sorry, your password is not correct, you have to enter pwd, that should be more than 8 and less than 20 char")
# else:
#     print("Sorry, include alpha and numaric in your password")
#
# list=[]
# s=input("Enter ")
# if (len(s)>=8):
#     for i in s:
#         if i.isupper():
#             list.append(i)
#         if i.islower():
#             list.append(i)
#         if i.isdigit():
#             list.append(i)
#         if(i=='@'or i=='_'or i=='$' or i=='+'):
#             list.append(i)
#         if len(list)==len(s):
#             print("valid password")
# else:
#     print("invalid password")
#
# 4.2
# import re
# p= input("Input your password ")
# x = True
# while x:
#     if (len(p)<8 or len(p)>20):
#         break
#     elif not re.search("[a-z]",p):
#         break
#     elif not re.search("[0-9]",p):
#         break
#     elif not re.search("[$#@]",p):
#         break
#     elif re.search("\s",p):
#         break
#     else:
#         print("Valid Password")
#         x=False
#         break
#
# if x:
#     print("Not a Valid Password")

# 5.1 get and remove student name
# lst=[]
# for i in range(10):
#     name=input()
#     lst.append(name)
# print(lst)
# std_name=input()
# lst.remove(std_name)
# print(lst)

# 5.2 get and update student name
# lst=[]
# for i in range(1,11):
#     name=input()
#     lst.append(name)
# print(lst)
# name2=int(input())
# std_name=input()
# lst[name2]=std_name
# print(lst)
#
# 6.i.update a specific key and remove dictionary values
# dict={"name":"harrish","age":22,"corse":"python"}
# oldkey=input("oldkey is")
# newkey=input("new key is")
# dict[newkey]=dict[oldkey]
# del dict[oldkey]
# print(dict)
#
# 6.ii. total length of the dictionary keys and values
# dict={"name":"harrish","age":22,"corse":"python"}
# print(len(dict.keys()))
# print(len(dict.values()))

# 7.1 Check the email is proper or not
# import re
# emailid=input('Please enter your email id :')
# x = re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', emailid)
# if x:
#     print('email is valid')
# else:
#     print('email is not valid')

# 7.2 URL is Valid or Not Valid
# import re
# url_id=input('enter the url: ')
# regex="^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$"
# x = re.search(regex,url_id)
# if x:
#     print('URL is Valid')
# else:
#     print('URL is Not valid')

# 8.1 reverse a substring from a string
# word = input('enter a string: ')
# start =int(input('enter the start:'))
# end=int(input('enter the end:'))
# revers=word[start:end]
# print(revers[::-1])

# 8.2 strong password generator and password length is declared by the user
# import random
# import string
# letters=string.ascii_letters
# numbers1=string.digits
# punctation=string.punctuation
# n_letters=int(input('enter how many letters: '))
# n_num=int(input('enter how many numbers: '))
# n_pun=int(input('enter how many symbols: '))
# passlist=[]
# for i in range(1,n_letters+1):
#     passlist+=random.choice(letters)
# for i in range(1,n_num+1):
#     passlist+=random.choice(numbers1)
# for i in range(1,n_pun+1):
#     passlist+=random.choice(punctation)
# random.shuffle(passlist)
# password=""
# for i in passlist:
#     password+=i
# print(password)

# 9.1 sort dictionary by keys
# case sensitive while sorting number,uppercase, lowercase is a priority
# dict={"name":"Harrish","age":"20","course":"Python","city":"chennai"}
# print(dict)
# print(sorted(dict.items()))
# print(sorted(dict.keys()))

# 9.2 sort dictionary by keys
# print(sorted(dict.values()))

# 10.1 program to find gravitational force
# m1 = float(input('mass of the object 1 '))
# m2 = float(input('mass of the object 2 '))
# r = float(input('enter the radius '))
# product = m1 * m2
# g = 0.00000000006674
# force = (g*(m1 * m2))/r*r
# print(str(force) + "N")

# Get a length in mm and convert to m and km
mm=float(input('enter the length in mm: '))
m=mm*0.001
km=mm*0.000001
print("Millimeter "+str(mm)+"is converted into "+str(m)+" meters")
print("Millimeter "+str(mm)+"is converted into "+str(km)+" kilometers")