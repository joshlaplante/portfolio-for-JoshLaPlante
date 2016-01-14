#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?



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

def getLargestPrime(N):
    return max(primeFactorize(N))
