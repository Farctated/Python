def solution(lst):
    c = [0] * len(lst)
    count = 0
    for i in range(0,len(lst)):
        for j in range(0, i):
            if lst[i] % lst[j] == 0:
                c[i] = c[i] + 1
                count = count + c[j]
    print(c)


    return count
print(solution([1,2,3,4,5,6]))