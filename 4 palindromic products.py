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
