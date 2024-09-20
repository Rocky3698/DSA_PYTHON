def sumOfDigits(n):
    assert n>=0 and int(n) == n, 'Number must be positive integer'
    if n<10:
        return n
    else:
        return (n%10) + sumOfDigits(n//10)
    
print(sumOfDigits(123.5))