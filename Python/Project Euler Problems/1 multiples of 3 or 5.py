#If we list all the natural numbers below 10 that are multiples of 3 or 5,
#we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.


def multiples(mult1,mult2,Num):
    i=0
    multiplesList=[]
    while i<Num:
        if i%mult1==0 or i%mult2==0:
            multiplesList.append(i)
        i+=1
    return sum(multiplesList)

#this function takes two numbers as parameters to check for multiples of them
#starting at 1 and increasing by 1 at every iteration,
#as well as one number as the upper limit at which to stop checking for
#multiples. the multiples that are found are inserted into the multiplesList,
#and the sum of the multiples in this list are returned. for this problem,
#the function should be run as multiples(3,5,1000) to first find all multiples
#of either 3 or 5 below 1000, then return their sum.
