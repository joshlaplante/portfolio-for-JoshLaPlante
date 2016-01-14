#The sum of the squares of the first ten natural numbers is,

#1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is,

#(1 + 2 + ... + 10)^2 = 552 = 3025
#Hence the difference between the sum of the squares of the first
#ten natural numbers and the square of the sum is 3025 − 385 = 2640.

#Find the difference between the sum of the squares of the first
#one hundred natural numbers and the square of the sum.




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
  
        
