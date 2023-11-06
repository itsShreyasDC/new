infile=open("D:\\infile.txt","r")
d={}
lines=infile.readlines()
for line in lines:
    words=line.split()
    for word in words:
        if word in d:
            d[word]+=1
        else:
            d[word]=1
for i in d.keys():
    print(i,":",d[i])


