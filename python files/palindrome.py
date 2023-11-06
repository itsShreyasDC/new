num=input("enter a num")
try:
    val=int(num)
    rev=str(num)[::-1]
    if num==rev:
        print("palindrome")
    else:
        print("not")
except:
    print("invalid")

   



