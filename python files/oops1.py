# class p:
#     def m1(self):
#         print("Parent")
# class c(p):
#     def m2(self):
#         print("Child")
# e1=c()
# e1.m1()
# e1.m2()

# class p1:
#     def m1(self):
#         print("Parent1")
# class p2:
#     def m2(self):
#         print("Parent2")
# class c(p1,p2):
#     def m3(self):
#         print("Child")
# e1=c()
# e1.m1()
# e1.m2()
# e1.m3()

class p:
    def m1(self):
        print("Parent1")
class c(p):
    def m2(self):
        print("Parent2")
class cc(c):
    def m3(self):
        print("Child")
e1=cc()
e1.m1()
e1.m2()
e1.m3()  



