# 1.
a = set((1,2,3,4,5))
b = set((3,2,6,5,5))
c = set((5,6,7,8,9))

print(a.union(b,c))

# 2.
print(a.difference(b,c))
print(b.difference(a,c))
print(c.difference(a,b))

3.
no1 = 10
no2 = 14
no3 = 16
no4 = 4
no5 = 15

if no1 > no2 and no1 > no3 and no1 > no4 and no1 > no5:
    print(F'Number 1 ({no1}) is max.')

if no2 > no1 and no2 > no3 and no2 > no4 and no2 > no5:
    print(F'Number 2 ({no2}) is max.')

if no3 > no1 and no3 > no2 and no3 > no4 and no3 > no5:
    print(F'Number 3 ({no3}) is max.')

if no4 > no1 and no4 > no2 and no4 > no3 and no4 > no5:
    print(F'Number 4 ({no4}) is max.')

if no5 > no1 and no5 > no2 and no5 > no3 and no5 > no4:
    print(F'Number 5 ({no5}) is max.')

# 4.
a = input("Enter the Alphabet from a to g: ")
if (a == "" or a != 'a' and a != 'b' and a != 'c' and a != 'd' and a != 'e' and a != 'f' and a != 'g'):
    print("Enter Valid Input")
else:
    if (a == "a"):
        print("Apple")
    if (a=='b'):
        print("Ball")
    if (a=='c'):
        print("Cat")
    if (a=='d'):
        print("Doll")
    if (a=='e'):
        print("Elf")
    if (a=='f'):
        print("Fan")
    if (a=='g'):
        print("Girl")
# if (a != 'a' and a != 'b'):
#     print ("Enter valid input")