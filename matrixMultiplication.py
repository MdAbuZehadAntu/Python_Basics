from numpy import *
row = int(input("Row : "))
col = int(input("Column : "))
A=[]
B=[]
p
for i in range(row):
    c=[]
    for j in range(col):
        c.append(int(input("Enter value in A ["+str(i)+"]["+str(j)+"] : ")))

    A.append(c)
print("A : ")
print(A)
for i in range(row):
    for j in range(col):
        print(str(A[i][j])+" ",end="")
    print()


for i in range(row):
    c=[]
    for j in range(col):
        c.append(int(input("Enter value in B ["+str(i)+"]["+str(j)+"] : ")))

    B.append(c)
print("B : ")
for i in range(row):
    for j in range(col):
        print(str(B[i][j])+" ",end="")
    print()



m=[]

for i in range(row):
    d=[]
    for j in range(col):
        sum=0;

        for x in range(row):
            sum+=A[i][x]*B[x][j]
        d.append(sum)
    m.append(d)



print("Product of the matrix is : ")

for i in range(row):
    for j in range(col):
        print(str(m[i][j])+" ",end="")
    print()




