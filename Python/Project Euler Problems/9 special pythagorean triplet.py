#A Pythagorean triplet is a set of three natural numbers,
#a < b < c, for which,

#a^2 + b^2 = c^2

#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.




def main():
    limit = 1000
    for i in range(1,limit):
        for j in range(i,limit-i):
            k = limit - i - j
            if i*j == ((500-k)*1000):
                print('triplet:', i,j,k, 'product:', i*j*k)
                


if __name__ == "__main__": main()


#Given that a^2 + b^2 = c^2, and a + b + c = 1,000, we can do a bit of math to
#simplify the process for checking for a Pythagorean triplet.
#
# Starting with:
# a + b + c = 1,000
# let's first reorganize the terms to:
# a + b = 1,000 - c
# then square both sides:
# a^2 + 2*a*b + b^2 = 1,000,000 - 2,000*c + c^2
# then use the fact that a^2 + b^2 = c^2 to substitute on the left side:
# c^2 + 2*a*b = 1,000,000 - 2,000*c + c^2
# then subtract c^2 from both sides:
# 2*a*b = 1,000,000 - 2,000*c
# next divide every term by 2:
# a*b = 500,000 - 1,000*c
# and finally factor out 1,000 from the terms on the right:
# a*b = (500-c)*1,000
#
#This resulting equation is what we will use to check if 3 terms that sum to
#1,000 are a Pythagorean triplet. This allows us to avoid using exponentiation
#and should speed up the checking process a bit.
#
#the main function here first sets the limit that the 3 terms should sum to,
#in this case 1,000. a for loop then iterates through values for the first term
#from 1 up to but not including 1,000, and a nested for loop iterates through
#values for the second larger term, starting from the first lower term up to
#but not including the difference between 1,000 and the lower term, since they
#must sum to 1,000. the last term is then assigned the remaining difference
#between 1,000 and the first two terms. the Pythagorean triplet checking formula
#derived above is then used to check if the current 3 terms form a triplet,
#and if they do, the triplet and the product of the triplet is then printed.
