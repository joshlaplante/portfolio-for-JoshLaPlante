#A palindromic number reads the same both ways.The largest palindrome
#made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.



def palindromeTester(num):
    if str(num) == str(num)[::-1]:
        return True

def largestPalindromeProduct(minNum,maxNum):
    palindromeProductList = []
    for i in range(minNum,maxNum+1):
        for j in range(minNum,maxNum+1):
            if palindromeTester(i*j) == True:
                palindromeProductList.append(i*j)
    return max(palindromeProductList)
