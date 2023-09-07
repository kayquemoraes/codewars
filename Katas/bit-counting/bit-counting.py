def count_bits(n):
    if n >= 0:
        s = 0
        while n > 0:
            s += n%2
            n = int(n/2)
        return s
    else:
        return False