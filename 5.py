#write a program to check given number is prime or not
# 2 3 5 7 11 13 17 19 .......
count=0
num=int(input("enter your number to check it is prime or not:"))
for i in range(1, (num//2)+1):
    if num%i==0:
        count=count+1
if count==1:
   print(num,"is prime number")
else:
    print(num,"is not prime number")
