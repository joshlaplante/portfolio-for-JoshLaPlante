def multiples(j,k):
    i=1
    multiplesList=[]
    while i<1000:
        if i%j==0 or i%k==0:
            multiplesList.append(i)
        i+=1
    return sum(multiplesList)

