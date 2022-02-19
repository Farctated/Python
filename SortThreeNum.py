# array = [1,0,0,-1,-1,0,1,1]
# sorted = [0,1,-1]

# mix_word = input("What are your mixed characters: \n")
# phrase = input("What word would like to like: \n")


# def make_word(character, word):
#     if len(character) <= 0:
#         return False
#     if len(word) == 0:
#         return True
#     ch_array = list(character)
#     for i in word:
#         if i in ch_array:
#             ch_array.pop(ch_array.index(i))
#         else:
#             return False
#     return True
# print(make_word(mix_word, phrase))

# def threeNSort(a, sorted):
#     array = a
#     new_array = []
#     for i in sorted:
#         while i in array:
#             index = array.pop(array.index(i))
#             new_array.append(index)
#     return new_array
# print(threeNSort(array,sorted))



#new_array = [i for i in array if i < 10]

#new_array = [x for x in array if x < 10]
#print(new_array)
# def solution(array):
#     new_array = array
#     first = 0
#     second = 0
#     third = 0
#     for i in new_array:
#         if i > first:
#             first = i
#     new_array.pop(new_array.index(first))
#     second = i for i in new_array if i > second
#     new_array.pop(new_array.index(second))
#     for i in new_array:
#         if i > third:
#             third = i
#     new_list = new_array
#     print(new_list)
#     return [first, second, third]
# print(solution(array))

# arrays = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

# def solution(a):
#     array = a
#     count = 0
#     result = []
#     while count< 3:
#         target = float('-inf')
#         for i in array:
#             if i > target:
#                 target = i
#         array.pop(array.index(target))
#         result.append(target)
#         count += 1
#     return result

# print(solution(arrays))
'''
Write a function that takes in a "special" array and returns its product sum.
A "special" array is a non-empty array that contains either integers or other "special" arrays. The
product sum of a "special" array is the sum of its elements, where "special" arrays inside it are
summed themselves and then multiplied by their level of depth.

The depth of a "special" array is how far nested it is. For instance, the depth of [] is 1; the depth
of the inner array in [[]] is 2; the depth of the innermost array in [[L]]] is 3

Therefore, the product sum of [x, y] is x + y; the product sum of [x, 2[y, z]] is
x + 2 * (y + z) ; the product sum of [x, [y, [z]]] is x + 2 * (y + 3z)
array = [5, 2, (7, -1], 3, [6, [-13, 8], 4]][-13, 8]
Sample Output 12 // calculated as:  5 +2+2 * (7-1)+3 + 2*6+3*（-13+8)+4)
'''

# array =[5, 2,[7,-1], 3, [6, [-13,[4,2],8],4]]

# def productSum(l):
#     count = 1
#     proSum = 0
#     for i in l:
#         if type(i) == list:
#             count +=1
#             proSum += count*i
#         else:
#             proSum += count
#     return proSum

# print(productSum(array))
def solution(str):
    sums = str
    hundred = 0
    fifty = 0
    twenty = 0
    remainder = sums % 100
    if remainder == 30 or remainder == 10:
        hundred = ((sums - remainder) / 100) - 1
        remainder = remainder + 1
        remainder = remainder - 50
        fifty += 1
    elif 30 < remainder<100:
        hundred = ((sums - remainder) / 100)
        twenty = remainder / 20
    else:
        twenty = remainder / 20
    
    return [round(hundred), round(fifty),round(twenty)]
print(solution(230))


