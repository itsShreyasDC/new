from threading import *
def display():
    for i in range(1,5):
        print("child")
t=Thread(target=display)
t.start()
for i in range(1,5):
        print("main")
