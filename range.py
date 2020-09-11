p = int(input("Enter Number: "))
flag=1
for c in range(2,p):
    if p%c == 0 or p == 2 or p == 3:
        print("Not Prime!")
        flag=0
if flag==1:
    print("Prime")
