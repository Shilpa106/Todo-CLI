# Functions

# def print_func():
#     print("hello")
# # print_func()

# x=print_func()
# print(x)

# def sum_of_two(num_1,num_2):
#     return num_1+num_2
# res = sum_of_two(2,4)
# print(res)


# # Functions with default arguments
# def greetings(name="Shilpa"):
#     print(f"Hello from {name}")
# greetings()
# greetings("Shilpi")



#Basic 


# classes = ['ds-algo','python','machine-learning','ama']
# for c in classes:
#     print(c, len(c),c.upper(),c.lower())

# for i in range(10):
    
#     print(f'Square of {i} is {i**2}')

# classes = ['ds-algo','python','machine-learning','ama']
# for index,c in enumerate(classes):
#     print(index,c, len(c),c.upper(),c.lower())


# print(sum(range(100)))
# print(list(range(1000)))

# while True:
#     pass

# i=0
# while i<10:

#     print(i)
#     i+=1

# def foo():
#     pass

# def fib(n):
#     if n<=1:
#         return n
#     return fib(n-1)+fib(n-2)

# fib(34)


# lecture_day =2
# print(lecture_day)


# square_area =36
# circle_area =6.28
# iota = (-1) ** (1/2)
# print(type(iota))
# print(square_area,circle_area,iota)

# greeting = "Hello from cli!"
# print(greeting)

# msg = "hello from "
# name = "Shilpa Yadav"
# print(f"{msg}{name}!")

# num1 = int(input())
# num2 = int(input())
# print(num1 + num2)
# x= None
# print(x)

# a=3
# less_than_3 = a<3
# print(less_than_3)
# print(type(less_than_3))

# a=4
# print(a==3)
# print(a!=3)

# x=5
# res_one =x<1 or x>10
# res_two =x>=1 and x<=10
# print(res_one)
# print(res_two)

# user_logged_in = True
# print(user_logged_in)

# x=bool(0)
# y=bool(-1)
# z=bool(1)
# print(x,y,z)

# print("Shilpa">"Shubham")
# print('s'>'S')
# print("Shilpa"=="Shubham")

# a="Shilpa"
# b="Shilpi"
# print(a is b)
# print(id(a))
# print(id(b))

# a=3
# b=5
# c=a&b
# print(c)

# a=False
# b=True
# c=True
# print(a or b and c)



# Conditionals
# x=int(input())
# if(x<1):
#     print('rude msg')
# if(x>10):
#     print('r msg')

# for n in range(10):
#     print(n,end=' ')
# print()


# for n in range(1, 11):
#     print(n, end=' ')
# print()

# for n in range(2,11,2):
#     print(n, end=' ')
# print()

# print(list(range(2,11,2)))

# counter = 0
# while(counter<10):
#     counter+=1
#     print(counter, end=' ')
# print()

# n=int(input())
# sum=0
# while(n>0):
#     d=n%10
#     sum+=d
#     n//=10
# print(sum)

# n=int(input())
# for multiple in range(1,11):
#     for number in range(1,n+1):
#         print(number*multiple, end=' ')
#     print()

# n=int(input())
# for multiple in range(1, 11):
#     for number in range(1, n+1):
#         print("%4d"%(number*multiple),end=' ')
#     print()


# names = ["Shilpa","In","dfd"]
# for name in names:
#     print(name)
#     if (name == "dfd"):
#         break

# names=input()
# for name in names:
#     if (name == "Shilpa"):
#         continue
#     print(name)


# 88888888888888

# names=input()
# target='i'
# for name in names:
#     print(f"{name} in outer loop")
#     for char in name:
#         if char == target:
#             print(f"Found {name} with letter: {target} ")
#             print("Breaking out of the inner loop")
#             break
#         break




