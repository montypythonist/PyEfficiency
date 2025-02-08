# PyEfficiency: omg silly functions like binary searches and algorithmic functions!! :D

# this is a binary search
def binarysearch(target, list):
    low = list[0]
    high = list[-1]
    middle = (high+low)/2
    while middle != target:
        middle = (high+low)/2
        if middle > target:
            high = middle - 1
        elif middle < target:
            low = middle + 1
    print(middle)