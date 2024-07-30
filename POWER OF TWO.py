def find_power_two(n):
    return n!=0 and (n&(n-1))==0

number=[16,17,32,33]
for i in number:
    if find_power_two(i):
        print(i,"is power of two")

    else:
        print(i,"is not power of two")
