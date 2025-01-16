i=0
j=1
sum=0
print(i,end="\t")
print(j,end="\t")
for a in range(11):
    sum=i+j
    print(sum,end='\t')
    i=j
    j=sum
