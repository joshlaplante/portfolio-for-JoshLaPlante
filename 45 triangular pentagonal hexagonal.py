def checkNum(N):
    triNumList=[]
    pentNumList=[]
    hexNumList=[]
    i=1
    for i in range(1,N+1):
        triNumList.append((i*(i+1))//2)
        pentNumList.append((i*((3*i)-1))//2)
        hexNumList.append(i*((2*i)-1))
        i+=1
    matchesList=[]
    for i in triNumList:
        if i in pentNumList and i in hexNumList:
            matchesList.append(i)
    return matchesList
    
