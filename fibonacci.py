def series(n):
    i=0
    j=1
    c=0
    if n==1:
        print(i)
    else:
        while c<n:
            print(i, end=" ")
            k=i+j
            i=j
            j=k
            c=c+1
            
n=int(input("enter the term"))
series(n)            