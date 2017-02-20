#The Fibonacci sequence is defined by the recurrence relation:

#Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#Hence the first 12 terms will be:

#F1 = 1
#F2 = 1
#F3 = 2
#F4 = 3
#F5 = 5
#F6 = 8
#F7 = 13
#F8 = 21
#F9 = 34
#F10 = 55
#F11 = 89
#F12 = 144

#The 12th term, F12, is the first term to contain three digits.

#What is the index of the first term in the Fibonacci sequence
#to contain 1000 digits?


def fibDigits(n):
    fib1 = 1
    fib2 = 1
    index = 2
    checkFib = 1
    while len(str(checkFib)) < n:
        checkFib = fib1 + fib2
        fib1 = fib2
        fib2 = checkFib
        index += 1
    return index

#the fibDigits function takes one number as a parameter, namely the
#number of digits you wish your Fibonacci number to contain, and it returns
#the index of the first Fibonacci number to contain that many digits.
#it does this by checking the number of digits in the current Fibonacci
#number computed, then computing the next Fibonacci number and increasing
#the index. once the desired number of digits is reached, the index of the
#last Fibonacci number computed is returned. calling fibDigits(1000) will
#produce the desired result
