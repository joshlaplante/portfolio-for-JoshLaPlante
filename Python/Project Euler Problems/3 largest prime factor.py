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

#the primeFactorize function takes a number to be decomposed into a list
#of its prime factors. starting with 2 as the divisor, the number to be
#decomposed is divided evenly as many times as possible by the divisor,
#and for each successful division, that divisor is added to the primeFactorList.
#after a remainder is reached from division by the divisor, the divisor is
#increased and the process is repeated, until the square of the divisor
#is as large as the number being decomposed. the list of prime factors is
#then returned

def getLargestPrime(N):
    return max(primeFactorize(N))

#simply pulls the largest prime factor from the list of prime factors
#created by the primeFactorize function. for this problem, we call on the
#getLargestPrime function as getLargestPrime(600851475143).
