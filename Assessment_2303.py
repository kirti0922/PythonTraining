# pal=input("Enter input for palindrome: ")
# rev =''
# for i in range(len(pal)-1,-1,-1):
#     rev=F"{rev}{pal[i]}"
#     # print(rev)
# # print(pal)
# # print(rev)
# if pal == rev:
#     print(F"Input {pal} is Palindrome")
# else:
#     print(F"Input {pal} is not a Palindrome")


prime_num=int(input("Enter a number: "))
print("prime numbers are :")
for i in range(1,prime_num+1):
    cnt=0
    for j in range(1,i+1):
        if i%j == 0:
            cnt += 1
    if cnt == 2:
        print(i)


