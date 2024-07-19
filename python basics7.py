#PRIME NUMBER

value=int(input("ENTER THE VALUE:"))
count=0
for i in range(2,value):
    if value%i==0:
        count=count+1

if count==0:
    print(value,"is prime")

else:
    print(value,"is not prime")
