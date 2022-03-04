array = [1,0,0,-1,-1,0,1,1]
sorted = [0,1,-1]
def threeNSort(a, sorted):
    array = a
    new_array = []
    for i in sorted:
        while i in array:
            index = array.pop(array.index(i))
            new_array.append(index)
    return new_array
print(threeNSort(array,sorted))