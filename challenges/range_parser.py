"""
Implement a function that returns an inclusive list of numbers
from a Python slice style string with 1 <= N <= 10.

    '1'      # returns [1]
    ':7'     # returns [1, 2, 3, 4, 5, 6, 7]
    '8:'     # returns [8, 9, 10]
    '2:5'    # returns [2, 3, 4, 5]
    'a:b'    # returns 'Range values must be integers!'
    '1:2:3'  # returns 'Only two values allowed!'

"""


def range_parser(s):
    """Returns an inclusive list of numbers from a Python slice style string with 1 <= N <= 10."""
    stringList = list(s)

    tooManyArgs = len(stringList) > 3    
    if tooManyArgs:
        return 'Only two values allowed!'
    
    toNumber = stringList[0] == ':'
    fromNumber = stringList[len(stringList) - 1] == ':'

    filteredList = filter(None, list(s.replace(':', '')))

    for string in filteredList:
        if string.isalpha():
            return 'Range values must be integers!'

    start = int(filteredList[0])
    end = int(filteredList[len(filteredList) - 1]) + 1

    if toNumber:
        return range(1, end)
    elif fromNumber:
        return range(start, 11)    
    else:
        return range(start, end)
        
