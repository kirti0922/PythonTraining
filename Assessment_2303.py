pal=input("Enter input for palindrome: ")
rev =''
for i in range(len(pal)-1,-1,-1):
    rev=F"{rev}{pal[i]}"
    # print(rev)
# print(pal)
# print(rev)
if pal == rev:
    print(F"Input {pal} is Palindrome")
else:
    print(F"Input {pal} is not a Palindrome")


# prime_num=int(input("Enter a number: "))
#
# for i in range(1,prime_num+1):
#     cnt=0
#     con=""
#     for j in range(1,i+1):
#         if i%j == 0:
#             # print(j )
#             # print(i)
#             cnt += 1
#
#         if cnt == 2:
#             con = F"{i} {con}"
#
# if cnt == 2:
#         print(F"Number 0 , 1 , {prime_num}  are prime number")
# else:
#         print(F"Number {prime_num} is not prime number")



