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
