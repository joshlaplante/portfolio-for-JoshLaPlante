#If we list all the natural numbers below 10 that are multiples of 3 or 5,
#we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.


def multiples(j,k):
    i=1
    multiplesList=[]
    while i<1000:
        if i%j==0 or i%k==0:
            multiplesList.append(i)
        i+=1
    return sum(multiplesList)

