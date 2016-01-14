def sumSquareDiff(N):
    squaresList=[]
    numsList=[]
    i=1
    for i in range(N+1):
        squaresList.append(i*i)
        numsList.append(i)
    sumOfSquares=sum(squaresList)
    sumOfNums=sum(numsList)
    squareOfSum=sumOfNums**2
    return squareOfSum - sumOfSquares
  
        
