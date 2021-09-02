# given a list of strings, find lengths of each of them
names = ["Shilpa","Shilpi"]
len_list=[]
for name in names:
    len_list.append(len(name))
# print(len_list)


# Using list comprehension
len_list = [len(name) for name in names]
len_list = [("length", len(name)) for name in names]
# print(len_list)


# with odd length
len_list =[("length", len(name)) for name in names if len(name)%2==1]
# print(len_list)

# sum of all even number from 1 to 100
sum_even = sum([num for num in range(1,101) if num % 2 == 0])
print(sum_even)