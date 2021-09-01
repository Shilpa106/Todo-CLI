# f=open("hello.txt",'r')
# print(f.read(5))
# print(f.readline())
# print(f.readlines())


# print(f.tell())  # get the current file position

# print(f.seek(0))
# f=open("hello1.txt","w")

# f.write("hello world..................\n")
# f.close()
# f.write("hey shilpi")


# # Open file using context manager
# with open('hello.txt', 'w') as f:
#     f.write("heyyy its open file using context manager ")


# # Reading CSV File
# import csv
# with open('marks.csv','r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


# # Writing to CSV file
# import csv
# with open('marks.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Roll No.", "Name", "Marks"])
#     writer.writerow([1,'abc',87])
#     writer.writerow[2,'def',80]


# # Read file as a dictionary
# import csv
# with open('marks.csv','r') as file:
#     csv_dict = csv.DictReader(file)
#     for row in csv_dict:
#         print(row)


# same  DictWriter
# pandas

# # Working with JSON Files

# # Reading json from file

# import json
# with open('marks.json') as file:
#     data = json.load(file)
#     print(data)

# # Notes
# # json.loads can be used to convert string to dict.
# # json.dumps can be used to convert dict to string.
# # Can pass indent and sort_keys properties to pretty print the json data.
# # Writing json to file
# import json

# marks_dict = {
#     "roll_no":12,
#     "name":"shilpi",
#     "marks":999
# }
# with open('marks.json','w') as json_file:
#     json.dump(marks_dict, json_file)




