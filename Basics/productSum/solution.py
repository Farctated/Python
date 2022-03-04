array =[5, 2,[7,-1], 3, [6, [-13,[4,2],8],4]]

def productSum(l):
    count = 1
    proSum = 0
    for i in l:
        if type(i) == list:
            count +=1
            proSum += count*i
        else:
            proSum += count
    return proSum

print(productSum(array))