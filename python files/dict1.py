line=input("Enter a line")
d={}
for c in line:
    if c in d:
        d[c]+=1
    else:
        d[c]=1
for key in d.keys():
    print(key,":",d[key])



   



