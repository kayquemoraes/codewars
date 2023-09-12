def sum_two_smallest_numbers(numbers):
    
    low = numbers[0]
    more = numbers[0]
    second = numbers[0]
    
    for i in numbers:
        if i < low:
            low = i
    
    for i in numbers:
        if i > more:
            more = i
    
    for i in numbers:
        if i> low and i<more:
            more = i
            second = more
    
    return low + second
        
        