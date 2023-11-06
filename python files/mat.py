a=[[1,2,3],[4,4,5],[1,1,1]]
b=[[1,0,3],[4,0,5],[0,1,1]]
c=[[0,0,0],[0,0,0],[0,0,0]]   

for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j]=a[i][j]+b[i][j]
for r in c:
    print(r)



