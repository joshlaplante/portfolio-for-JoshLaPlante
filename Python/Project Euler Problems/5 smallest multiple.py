#2520 is the smallest number that can be divided by each of the numbers
#from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all
#of the numbers from 1 to 20?




#this problem is asking us to find the LCM (least common multiple) of all the
#numbers from 1 to 20, and to simplify ever so slightly, this is the same as
#finding the LCM of all numbers from 2 to 20.
#to do this, we will need to analyze the prime factorization of each number
#from 2 to 20, and for every prime that comes up, we will keep track of the
#highest power of that prime that has occured. the product of every prime
#raised to its highest power will then be the LCM we are looking for.

#for example, consider the LCM of 9 and 21. by prime factorizing, we see that
#9 = 3^2, and 21 = 3^1 * 7^1. the highest power of 3 that occurs is 3^2, and
#the highest power of 7 that occurs is 7^1, so we take their product, 63, as
#the least common multiple or LCM of 9 and 21.

#to start on this problem we need a function that can prime factorize any
#number

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

#now we need a function that can keep track of the highest power of each
#prime that occurs accross the prime factorizations from 2 to 20.


def LCMprimeList(num):
    primeFactorSet = []
    for i in range(2,num+1):
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

#each number from 2 to the number inputted as num (in this problem, 20) is
#prime factorized one by one, and the highest power of each prime that comes
#up is kept in the primeFactorSet. if a higher power of any prime already in
#primeFactorSet comes up during a later prime factorization, the higher power
#replaces the power of that prime.

        
def LCM(num):
    LCMprimeListForN = LCMprimeList(num)
    product = 1
    for i in LCMListForN:
        product*=i
    return product

#finds the LCM of all the numbers from 2 to num by multipling together the
#highest power of each prime kept in the primeFactorSet returned by the previous
#function.
