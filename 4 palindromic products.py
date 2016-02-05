#A palindromic number reads the same both ways.The largest palindrome
#made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.



def palindromeTester(num):
    if str(num) == str(num)[::-1]:
        return True

#the palindromeTester function takes a number as an argument then checks if
#that number reads the same forwards as it does when reversed, using string
#slicing to do the reversing.

def largestPalindromeProduct(minNum,maxNum):
    palindromeProductList = []
    for i in range(minNum,maxNum+1):
        for j in range(minNum,maxNum+1):
            if palindromeTester(i*j) == True:
                palindromeProductList.append(i*j)
    return max(palindromeProductList)

#this function checks all possible products of two numbers both ranging from
#minNum up to and including maxNum to see if those products are palindromic by
#calling the palindromeTester. the palindromic products found are inserted into
#the palindromeProductList, and the largest number from this list is then
#returned. in the context of this problem, we want the largest palindromic
#product of two 3-digit numbers, so we should call
#largestPalindromeProduct(100,999)
