months = ["jan","feb","march","april","may","june","july","august","september","october","november","december"]
count = 0
print("[",end="")
for m in months :
    count+=1
    if count > 4 :
        count=1
        print(m)
    else:
        print(m,end=" ")
print("]")