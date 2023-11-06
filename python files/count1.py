line=input("Enter")
nw=nd=nu=nl=0
words=line.split(" ")
nw=len(words)
for char in line:
    if char.isdigit():
        nd+=1
    if char.isupper():
        nu+=1
    if char.islower():
        nl+=1
print(nw,nd,nu,nl)

    



