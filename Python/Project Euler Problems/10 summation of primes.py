#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.




#prime numbers have only two divisors, namely 1 and themself. we will make use
#of that fact by creating a list of all numbers that have only two divisors,
#then summing the entries of the list

import math
import time

start_time = time.clock()
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
    composite = []
    primes = []
    i=2
    for i in range(2,N):
        if i not in composite:
            primes.append(i)
            for num in range(i*i, N, i):
                composite.append(num)
    print (max(primes))

primeList(200)
print (time.clock() - start_time, "seconds")
