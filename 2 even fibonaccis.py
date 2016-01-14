def evenFibs(num):
    fibsList = [1,2]
    n=1
    while fibsList[n]+fibsList[n-1]<num:
        n+=1
        i=(fibsList[n-1]+fibsList[n-2])
        fibsList.append(i)
    evenFibsList=[]
    for i in fibsList:
        if i%2==0:
            evenFibsList.append(i)
    return sum(evenFibsList)
    
