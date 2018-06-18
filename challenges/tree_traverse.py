"""
Given a deeply nested dict, create a function that returns a
value within a tree when given the tree and a dictKey. If there are
duplicates, the first result found should be returned.

    {
        'a': {
            'b': 123,
            'c': 456,
            'd': {
                'z': 789,
            },
        },
        'x': {
            'y': 111,
        },
    }  # input of 'z' should return '789'

"""


def tree_traverse(tree, key):
    """Traverse flat or neseted tree for a the value of the given key"""
    desiredLeaf = None

    for dictKey, value in tree.iteritems():
        if isinstance(value, dict):
            desiredLeaf = tree_traverse(value, key)
        if dictKey == key:
            desiredLeaf = value

    return desiredLeaf