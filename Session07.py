# varlist =[{'name': 'xyz', 'phone': 12343232, 'address': 'Pune','dob': '24/12/2016','education' : 'abc' }]
# print (varlist)
# varlist[0].update({'phone_no' : '12122323'})
# varlist.append('New Item')
# varlist.append({'K1': 'V1'})
# print (varlist)
# vardict ={'employee_no': '12', 'emp_id': 'emp_123232', 'name': 'emp name', 'skill_sets': ['QA', 'Python', 'SQL'],'dept_id' : 'D1' }
# print(vardict)
# vardict.update({'Sal': 10000,'Role' : 'DBA' , 'Exp' : '6 Years'})
# print(vardict)


a=input("Enter number 1:")
b=input("Enter number 2:")

print(type(a))
print(type(b))

if a>b:
    print(f"Maximum number is {a}")
elif a<b:
    print(f"Maximum number is {b}")
else :
    print(f"Both the numbers are same")

