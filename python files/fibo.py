def fibo(n):
   if n<=1:
      return n
   else:
      return(fibo(n-1)+fibo(n-2))
t=int(input("enter no of terms"))
if t<0:
   print("enter pos")
else:
   for n in range(t):
      print(fibo(n))
      

   



