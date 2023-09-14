def dig_pow(n, p):
    
    digits = str(n)
    sum = 0
    
    for i in range(len(digits)):
        sum += int(digits[i])**(p+i)
    
    if sum % n == 0:
        return sum / n
    else:
        return -1