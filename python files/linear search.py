n=int(input("enter no of terms"))
a=[]
for i in range(n):
    a.append(int(input("")))
key=int(input("enter key"))
flag=0
for i in range(n):
    if key==a[i]:
        flag=1
        pos=i+1
if flag==1:
    print("Found at",pos)
else:
    print("not found")



