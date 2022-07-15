import unittest

list_array = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
def solution(l):
    def compare(x):
        return list(map(int, (x.split('.'))))
    length = len(l)
    if length <= 1:
        return l
    else:
        comparison = l.pop()
    after_comparision = []
    before_comparision = []

    for item in l:
        if compare(item) > compare(comparison):
            after_comparision.append(item)
        else:
            before_comparision.append(item)
    return solution(before_comparision) + [comparison] + solution(after_comparision)

print(solution(list_array))
