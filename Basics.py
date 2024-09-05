import math
# val = float(input("Enter the value"))
# if(val > 100):
#     print("Yes")
# else : 
#     print("NO")
# print(abs(10))
# print(math.ceil(19.06))
# print(math.floor(-89.6))
# print(math.fabs(37.9))
# print(math.exp(5))
# print(math.log(10))
# print(math.log10(10))
# print(max(10,7,8))
# print(min(1,7,5))
# print(math.modf(2.89))
a =  int(input("Enter a number"))
flag = False
for i in range(2,a):
    if (a%i)==0  :
       flag = True
       break
if flag:
    print("no")
else:
    print("yes")

    
