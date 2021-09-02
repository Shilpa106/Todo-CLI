import os.path
print(os.path.abspath('.'))
import json
from datetime import datetime

FILE_NAME = 'lists.json'

def show_lists(args):
  with open(FILE_NAME, 'r') as lists_json:
    try:
      data = json.load(lists_json)
      # print(data)
      for index, todo_list in enumerate(data.keys()):
        print(index + 1, data[todo_list]['title'])
    except:
      print('Some error occurred!')

def use_list(args):
  list_name = args[0]
  with open(FILE_NAME, 'r') as lists_json:
    try:
      data = json.load(lists_json)
      l=[item for item in data if item['title']==list_name]
      if l:
            
            return f'{list_name}.json'
      else:
            return -1
    except Exception as e:
      
      print('Some error occurred!')
            

      # if (data.get(list_name)):
      #   return f'{list_name}.json'
      # else:
      #   return -1
    # except:
    #   print('Some error occurred!')

def create_list(args):
  list_name = args[0]
  # print(list_name,"***********************************************************************************************")
  # print(os.path.abspath('.'))
  new_list = {}
  # with open(FILE_NAME, 'r+') as lists_json:
  # print("35")
  try:
    # print("*********************")
    with open(FILE_NAME, 'r+') as lists_json:
      data = json.load(lists_json)
      # print(data)
      # check if file already exists
      b=["already created" for item in data if item['title']==list_name]
      print(b[0])


      # for item in data:
      #       # print(item['title'])
      #       if item['title']==list_name:
      #             print('List already exists! Try a different name...')
      #           # print("hey shilpaa fjdkjfjfjakjajf")
      #       else:
      #           # print("Byeeeee Shilpa")
      #           pass



      # if (data.get(list_name)):
      #   print('List already exists! Try a different name...')
      # else:
      #   # print("ccccccccccccccccc")
      #   pass
        # update the new_list dict
        
  except:
    with open(FILE_NAME, 'r+') as lists_json:
      data = json.load(lists_json)
      new_list = {'title': list_name,'created_at': datetime.now().strftime("%d/%m/%Y %H:%M:%S")}

        # print(new_list)
      # data[list_name] = new_list
      # print(data)
      data.append(new_list)
      # print(data)
      # /home/development/Documents/Todo Command Line Application/todoapp/commands/lists
      with open(f'{list_name}.json', 'w') as new_list:

      # with open('lists2.json', 'w') as new_list:
        # empty list
        new_list.write('[\n]')
        print('Successfully created the new list!')
      # add to the lists.json
      lists_json.seek(0)
      json.dump(data, lists_json, sort_keys=True, indent=True)

    # print('Some error occurred!')