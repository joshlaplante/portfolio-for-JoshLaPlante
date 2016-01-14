#2520 is the smallest number that can be divided by each of the numbers
#from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all
#of the numbers from 1 to 20?



def primeFactorize(N):
    primeFactorList = []
    divisor = 2
    while divisor**2 <= N:
        while N%divisor == 0:
            primeFactorList.append(divisor)
            N//=divisor
        divisor+=1
    if N >1:
        primeFactorList.append(N)
    return primeFactorList


def LCMList(num):
    primeFactorSet = []
    i=2
    for i in range(num):
        currentPrimeList = primeFactorize(i)
        for j in currentPrimeList:
            if j not in primeFactorSet:
                primeFactorSet.append(j)
            if j in primeFactorSet:
                currentCount = currentPrimeList.count(j)
                setCount = primeFactorSet.count(j)
                if currentCount > setCount:
                    difference = currentCount - setCount
                    for i in range(difference):
                        primeFactorSet.append(j)
    primeFactorSet.sort()
    return primeFactorSet
        
def smallestMultiple(N):
    LCMListForN = LCMList(N)
    product = 1
    for i in LCMListForN:
        product*=i
    return product
