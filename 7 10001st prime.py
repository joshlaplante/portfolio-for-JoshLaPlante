#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
#see that the 6th prime is 13.

#What is the 10,001st prime number?




import math

def divisorNum(N):
    divisors=[1,N]
    rootN=math.sqrt(N)
    i=2
    while i<rootN:
        if N%i==0:
            divisors.append(i)
            divisors.append(N//i)
        i+=1
    if N%rootN==0:
        divisors.append(rootN)
    divisors.sort()
    return divisors



def primeList(num):
    primes=[]
    i=1
    while len(primes)<num:
        d=divisorNum(i)
        if len(d)==2:
            primes.append(i)
        i+=1
    return primes[num-1]
    
