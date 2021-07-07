n=input("enter full name")
i=0
temp=""
while i<len(n):
    if n[i] not in temp:
        temp+=n[i]
        print(f"{n[i]}:{n.count(n[i])}")
    i+=1