# Factorial number
# def fact(n):
#     return 1 if (n == 1 or n == 0) else n * fact(n - 1)
# num = int(input('enter the factorial number: '))
# print('The factorial of {0} is {1}'.format(num, fact(num)))

# print the ASCII value of assigned character in c
# c = input('enter thr string: ')
# print("The ASCII value of '" + c + "' is", ord(c))

# Python program to print all prime number in an interval
# def prime(x, y):
#     prime_list = []
#     for i in range(x, y):
#         if i == 0 or i == 1:
#             continue
#         else:
#             for j in range(2, int(i / 2) + 1):
#                 if i % j == 0:
#                     break
#             else:
#                 prime_list.append(i)
#     return prime_list
#
#
# starting_range = int(input('Enter the starting range: '))
# ending_range = int(input('Enter the ending range: '))
# lst = prime(starting_range, ending_range)
# if len(lst) == 0:
#     print("There are no prime numbers in this range")
# else:
#     print("The prime numbers in this range are: ", lst)


# find the largest number in the list
# a = [3, 8, 1, 7, 9, 5, 4]
# b = 0
# for i in a:
#     if b < i:
#         b = i
# print('The largest number is {}'.format(b))

# find the smallest number in the list
# c = a[0]
# for i in a:
#     if c > i:
#         c = i
# print('The smallest number is {}'.format(c))

# find the prime numbers
# n=int(input('enter the number: '))
# for i in range(2,n):
#     if n%i==0:
#         print('{} is not a Prime number'.format(n))
#         break
# else:
#     print('{} is a Prime number'.format(n))

# reverse string using for loop
stringinp=input(enter)

# 6.union three set
# a={5,12,52,0,8}
# b={2,5,1,9,8}
# c={4,5,6,0,10}
# d=a.union(b,c)
# print(d)

# 7.intersection of three set
# a = {5, 2, 4, 5, 7, 1}
# b = {5, 3, 11}
# c = {4, 5, 12, 2, 1, 0}
# print(a.intersection(b,c))

# 8. difference
# a={23,5,1,12,4,6,7}
# b={6,11,12,4,5,2,15,21,22,33}
# c=a.difference(b)
# print(c)

# 8.1 symmetric difference
# a = {12, 2, 0, 3, 8}
# b = {15, 10, 12, 3, 6}
# c = a.symmetric_difference(b)
# print(c)

# 9.Get number from user and display its tables
# def table(nums):
#     for i in range(1, 11):
#         print(str(i) + "*" + str(nums) + "=" + str(i * nums))
#
#
# num = int(input("enter the number:"))
# table(num)

# 9.1 get two numbers from user and display a table
# def table(nums,nums2):
#     for i in range(1, 11):
#         print(str(i) + "*" + str(nums) + "=" + str(i * nums))
#     print()
#     for j in range(1, 11):
#         print(str(j) + "*" + str(nums2) + "=" + str(j * nums2))
#
#
# num = int(input("enter the number:"))
# num2 = int(input("enter the number2:"))
# table(num,num2)
#
# 10.1. get 6 subjects marks from the user
# sub1=int(input("enter the mark"))
# sub2=int(input("enter the mark"))
# sub3=int(input("enter the mark"))
# sub4=int(input("enter the mark"))
# sub5=int(input("enter the mark"))
# sub6=int(input("enter the mark"))
# total=sub1+sub2+sub3+sub4+sub5+sub6
# avg=total/600
# print("total marks : "+str(total))
# print("avg marks : "+str(avg))
#
# 10.2. get 6 subjects marks from the user with percentage
# sub1=int(input("enter the mark "))
# sub2=int(input("enter the mark "))
# sub3=int(input("enter the mark "))
# sub4=int(input("enter the mark "))
# sub5=int(input("enter the mark "))
# sub6=int(input("enter the mark "))
# total=sub1+sub2+sub3+sub4+sub5+sub6
# avg=total/6
# print("total marks : "+str(total))
# print("avg marks : "+str(avg)+"%")

# 11.1 get two numbers max number
# n1=int(input("Enter the number: "))
# n2=int(input("Enter the number: "))
# if n1>n2:
#     print("1st number is greater that "+str(n1))
# else:
#     print("2nd number is greater that " + str(n2))
# print(max(n1,n2))

# 11.2 get three numbers max number
# n1=int(input("Enter the number: "))
# n2=int(input("Enter the number: "))
# n3=int(input("Enter the number: "))
# if n1>n2 and n1>n3:
#     print("1st number is greater that "+str(n1))
# elif n2>n1 and n2>n3:
#     print("2nd number is greater that " + str(n2))
# else:
#     print("3rd number is greater that " + str(n3))
# print(max(n1,n2,n3))

# 12.1 star pattern
# *
# **
# ***
# ****
# *****

# n=6
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# 12.2. Star pattern
#      *
#     **
#    ***
#   ****
#  *****
# ******
# n=6
# space=n
# for i in range(n):
#     for j in range(space+1):
#         print(end=" ")
#     for j in range(i+1):
#         print("*",end="")
#     print()
#     space=space-1
