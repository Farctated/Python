def solution(array):
    new_array = array
    first = second = third = 0
    for i in new_array:
        if i > first:
            first = i
    new_array.pop(new_array.index(first))
    for i in new_array:
        if i > second:
            second = i

    new_array.pop(new_array.index(second))
    for i in new_array:
        if i > third:
            third = i

    return [first, second, third]
### second solution
def solution_2(a):
    array = a
    count = 0
    result = []
    while count< 3:
        target = float('-inf')
        for i in array:
            if i > target:
                target = i
        array.pop(array.index(target))
        result.append(target)
        count += 1
    return result


arrays = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(f"From first solution: {solution(arrays)}")

array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(f"From second solution: {solution_2(array)}")