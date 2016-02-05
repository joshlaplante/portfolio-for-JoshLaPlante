#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
#see that the 6th prime is 13.

#What is the 10,001st prime number?



#prime numbers have only two divisors, namely 1 and themself. we will make use
#of that fact by creating a list of all numbers that have only two divisors,
#then returning the 10,0001st number from that list.


import math
def divisorList(N):
    if N == 1:
        divisors=[1]
    else:
        divisors=[1,N]
        rootN=math.sqrt(N)
        i=2
        while i<rootN:
            if N%i==0:
                divisors.append(i)
                divisors.append(N//i)
            i+=1
        if N%rootN==0:
            divisors.append(int(rootN))
    divisors.sort()
    return divisors

#this function creates a list of all divisors for a given number N by checking
#which numbers, if any, cleanly divide it, starting from 1 and working up to
#the square root of N. we only need to check up to the square root of N, because
#both the divisor and the quotient are added to the divisor list any time clean
#division occurs. if the number is a perfect square, the square root is inserted
#into the divisor list as well. 

def primeList(N):
    primes=[]
    i=1
    while len(primes)<N:
        d=divisorList(i)
        if len(d)==2:
            primes.append(i)
        i+=1
    return primes[N-1]

#this function returns the value of the Nth prime. starting at 1 and working up,
#the divisorList is called to see if a number is prime by checking if it has
#only two divisors, and if so, inserting that number to the list of primes.
#this is iterated until the primes list is populated by N primes, and then
#the Nth prime is returned. for this problem, we call the function as
#primeList(10001) to retreive the 10,001st prime.



