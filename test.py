months = ["jan","feb","march","april","may","june","july","august","september","october","november","december"]
count = 1
matrix = int(input("choose the matrix format \n 1.2X6 press 1 \n 2.3X4 press 2 \n 3.4X3 press 3 \n enter your choice: "))
print("[",end="")
for m in months :
    count+=1
    if count > matrix + 1 :
        count=1
        print(m)
    else:
        print(m,end=" ")
print("]")