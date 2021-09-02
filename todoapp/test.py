a=[{'created_at': '02/09/2021 15:28:42', 'title': 'djfj'}, {'created_at': '02/09/2021 15:30:17', 'title': 'dfdsjf'}, {'created_at': '02/09/2021 15:31:13', 'title': 'sjfkslj'}, {'created_at': '02/09/2021 15:33:25', 'title': 'jfdkljfajf'}, {'created_at': '02/09/2021 15:33:49', 'title': 'a'}, {'created_at': '02/09/2021 15:47:59', 'title': 'jfkdjfajdfj'}, 
{'created_at': '02/09/2021 15:50:50', 'title': 'jfkdjfajdfj'}, {'created_at': '02/09/2021 15:51:29', 'title': 'jfkdjfajdfj'}, {'created_at': '02/09/2021 15:52:47', 'title': 'jfkdjfajdfj'}, {'created_at': '02/09/2021 15:53:47', 'title': 'a'}, {'created_at': '02/09/2021 15:58:16', 'title': 'a'}]


# for item in a:
#     # print(item['title'])
#     if item['title']=='a':
#         print("hey shilpaa fjdkjfjfjakjajf")
#     else:
#         print("Byeeeee Shilpa")

# if a[0]['title']=='a':
#         print("hey shilpaa fjdkjfjfjakjajf")
# else:
#     print("Byeeeee Shilpa")

# b=["succcessfully created" for item in a if item['title']=='a']
# print(b[0])

data=[{'created_at': '02/09/2021 15:28:42', 'title': 'djfj'}, {'created_at': '02/09/2021 15:30:17', 'title': 'dfdsjf'}, {'created_at': '02/09/2021 15:31:13', 'title': 'sjfkslj'}, {'created_at': '02/09/2021 15:33:25', 'title': 'jfdkljfajf'}, {'created_at': '02/09/2021 15:33:49', 'title': 'a'}, {'created_at': '02/09/2021 15:47:59', 'title': 'jfkdjfajdfj'}, 
{'created_at': '02/09/2021 15:50:50', 'title': 'jfkdjfajdfj'}, {'created_at': '02/09/2021 15:51:29', 'title': 'jfkdjfajdfj'}, {'created_at': '02/09/2021 15:52:47', 'title': 'jfkdjfajdfj'}, {'created_at': '02/09/2021 15:53:47', 'title': 'a'}, {'created_at': '02/09/2021 15:58:16', 'title': 'a'}]
print(len(data))
for data1 in data:
    # print(data1.keys())
    z=data1['title']
    # print(z)
    for index,todo_list in enumerate(data1.keys()):
        # print(data1['title'])
        # print(len(data1['title']))
        # print(index+1,data1['title'])

        # print(todo_list)
        # print(index+1,todo_list)
        td=data1[todo_list]
        # print(td)
        print(index+1,td,' ')

        # print(td, end=' ')
        # print(type(td))
    print()


        # print(index + 1, td)










        # print(data1[todo_list])



        # print(data1[todo_list])
        # print(index + 1, data1[todo_list]['title'])
        # print(index+1,todo_list[0:len(z)+1])


    # print(type(data1.keys()))
    # for index, todo_list in enumerate(data1.keys()):
        # print(index + 1, data[todo_list]['title'])