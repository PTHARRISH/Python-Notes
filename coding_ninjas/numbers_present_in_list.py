'''
    Time Complexity: O( N * logN )
    Space Complexity: O( N )
    
    where N is the length of the list.
'''
def generatorFunction(numbersList):
    # Set which is used to know whether a element
    # is considered earlier or not
    elemPresent = set()
    
    for value in numbersList:
        curr = value
        if 2 * curr not in elemPresent:
            elemPresent.add(2 * curr)
            yield(2 * curr)
            
        if 2 * curr + 1 not in elemPresent:
            elemPresent.add(2 * curr + 1)
            yield(2 * curr + 1)


def generateNumbers(numbersList) -> list :
    # Sorting the given list
    numbersList.sort()
    
    # ans is the list which will store our final list
    ans = []
    
    for value in generatorFunction(numbersList):
        ans.append(value)
        
    return ans
    