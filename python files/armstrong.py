low=int(input("Enter lower"))
upp=int(input("Enter upper"))
for num in range(low,upp+1):
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    if num==sum:
        print(num)




