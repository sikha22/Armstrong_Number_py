#Armstrong number is like 153=1^3+5^3+3^3=1+125+27=153
n=int(input("Enter Number:"))
sum=0
order=len(str(n))
copy_n=n
while(n>0):
    digit=n%10
    sum+=digit**order
    n=n//10
if(sum==copy_n):
    print(f"{copy_n} is an Armstrong Number")
else:
    print(f"{copy_n}  is not an Armstrong Number")