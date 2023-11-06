infile=open("D:\\infile.txt","r")
lines=infile.readlines()
nl=nw=nc=0
nl=len(lines)
for line in lines:
    nc+=len(line)
    words=line.split()
    nw+=len(words)
print(nl,nw,nc)


