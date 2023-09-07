def binary_array_to_number(arr):
    sum = 0
    for i in range(len(arr)):
        if arr[len(arr) - i - 1] == 1:
            sum += 2 ** i
            
    return sum