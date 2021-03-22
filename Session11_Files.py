My_List=[{'name': 'xyz', 'phone': 12343232, 'address': 'Pune'}]
My_List.append({'name': 'Kirti', 'phone': 33443444, 'address': 'Pune'})
My_List.insert(1,{'name': 'Aaru', 'phone': 33443444, 'address': 'Pune'})
My_List.insert(1,{'name': 'Anu', 'phone': 33443444, 'address': 'Pune'})
My_List.insert(1,{'name': 'Seema', 'phone': 33443444, 'address': 'Pune'})
My_List.insert(1,{'name': 'Vaibhavi', 'phone': 33443444, 'address': 'Pune'})
My_List.insert(2,{'name': 'Jimy', 'phone': 33443444, 'address': 'Pune'})
# print(My_List)

my_dict= {'1': {'emp_id': 'emp_123232', 'name': 'emp name1', 'skill_sets': ['QA', 'Python', 'SQL']}}
my_dict.update({'2': {'emp_id': 'emp_22323', 'name': 'emp name2', 'skill_sets': ['QA', '.NET', 'SQL']}})
my_dict.update({'3': {'emp_id': 'emp_22763', 'name': 'emp name3', 'skill_sets': ['QA', '.NET', 'SSAS']}})
my_dict.update({'4': {'emp_id': 'emp_22345', 'name': 'emp name4', 'skill_sets': ['SSIS', '.NET', 'SQL']}})
my_dict.update({'5': {'emp_id': 'emp_22346', 'name': 'emp name5', 'skill_sets': ['SSRS', '.NET', 'SQL']}})
#print(my_dict)

import os

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
#print(BASE_PATH)

# ASSET_PATH = BASE_PATH + '/'  + 'assets' # Not recommended
ASSET_PATH = os.path.join(BASE_PATH, 'assets')
#print(ASSET_PATH)



if not os.path.exists(ASSET_PATH):
    os.makedirs(ASSET_PATH)

JSON_FILE_PATH1 = os.path.join(ASSET_PATH, 'Test.json')
JSON_FILE_PATH2 = os.path.join(ASSET_PATH, 'Employee_Dict.json')
import json
with open(JSON_FILE_PATH1, 'w') as _file:
    json.dump(obj=My_List, fp=_file)
print("Employee Json file with List created successfully")
with open(JSON_FILE_PATH2, 'w') as _file:
    json.dump(obj=my_dict, fp=_file)
print("Employee Json file with Dict created successfully")

emp = [['emp_no', 'emp_name', 'sal', 'dept'],
    [1, 'abc', 1000, 'D1'],
    [2, 'qwe', 1500, 'D2'],
    [3, 'dfg', 1100, 'D1'],
    [4, 'zxc', 1200, 'D1'],
    [5, 'iop', 1300, 'D2']]

import csv
CSV_FILE = os.path.join(ASSET_PATH, 'emp_csv.csv')
with open(CSV_FILE, 'w',newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(emp)

print("emp_csv created successfully")

with open(CSV_FILE, 'r') as _file:
    csv_read = csv.reader(_file)
    for i in csv_read:
        print(i)
