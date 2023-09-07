def array_diff(a, b):
    array = []
    for i in range(len(a)):
        if a[i] not in b:
            array.append(a[i])
    return array