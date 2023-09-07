def solution(n):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    sym = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    
    s = ""
    i = 0

    while n > 0:
        while n >= val[i]:
            s += sym[i]
            n -= val[i]
        i += 1

    return s