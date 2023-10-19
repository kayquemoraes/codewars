def sum_array(arr):
    if arr is None or len(arr) <= 1:
        return 0
    else:
        max = arr[0]
        min = arr[0]
        sum = 0

        for i in arr:
            if i > max:
                max = i
            if i < min:
                min = i
            sum += i

        return sum - (max + min)