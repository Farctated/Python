def solution(s):
    # cut slices into parts
    # check the length is not odd
    # make sure no remainder is left
    # create an array/list of equal slices
    # return the number of item in the list/slices
    
    l = len(s)
    for i in range(1,l):
        if l % i == 0:
            equal_parts = [s[j:j+i] for j in range(0,l,i)]
            if equal_parts[1:] == equal_parts[:-1]:
                return len(equal_parts) 
    return 1

print(solution("abaabaabaabaaba"))

