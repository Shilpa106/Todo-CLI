# fruits = ["apple","banana","cherry","kiwi","mango"]
# newlist = []
# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
        
# # print(newlist)

# newlist1 = [x for x in fruits if "a" in x]
# print(newlist1)



# newlist = [x for x in fruits if x != "apple"]
# print(newlist)


# newlist = [x for x in fruits]
# print(newlist)


# newlist = [x for x in range(10)]
# print(newlist)


# newlist = [x for x in range(10) if x<5]
# print(newlist)


# newlist = [x.upper() for x in fruits]
# print(newlist)

# newlist = ['hello' for x in fruits]
# print(newlist)

# newlist = [x if x!= "banana" else "orange" for x in fruits]
# print(newlist)


# thislist = ["orange","mango","kiwi","pineapple","banana"]
# thislist.sort()
# print(thislist)

# def myfunc(n):
#     return abs(n-50)

# thislist = [100,50,65,82,23]
# thislist.sort(key=myfunc)
# print(thislist)

thislist = ["apple","banana","cherry","jam"]
# mylist = thislist.copy()
# print(mylist)

# mylist=list(thislist)
# print(mylist)


# list1=["a","b","c"]
# list2=[1,2,3]
# list3=list1+list2
# print(list3)

# fruits=("apple","banana","cherry")
# (green,yellow,red) = fruits
# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green,yellow,*red)=fruits
# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)

# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)



# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#   print(thistuple[i])


# thistuple = ("apple", "banana", "cherry")
# i = 0
# while i < len(thistuple):
#   print(thistuple[i])
#   i = i + 1


# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)

# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2

# print(mytuple)

thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964,
    "year":2020
}
# print(thisdict)
# print(thisdict["brand"])

# x=thisdict["model"]
# x=thisdict.get("model")
# x=thisdict.keys()
# thisdict["color"]="White"
# print(x)


# x=thisdict.values()
# x=thisdict.items()
# print(x)
# thisdict["year"]=2021
# print(x)

# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")

# thisdict.update({"year":2020})
# thisdict.update({"color":"red"})

# thisdict.pop("model")
# thisdict.popitem()
# del thisdict["model"]
# thisdict.clear()
# print(thisdict)


# def my_func(x):
#     return 5*x

# print(my_func(3))
# print(my_func(5))
# print(my_func(9))


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1=Person("john",46)
# print(p1.name)
# print(p1.age)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " +self.name)

p1=Person("john",36)
p1.myfunc()

