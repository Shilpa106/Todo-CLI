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

b=["succcessfully created" for item in a if item['title']=='a']
print(b[0])