"""
Implement a class that can convert a Python dictionary into an object.

    {
        'a': 1,
        'b': {
            'c': 2,
        },
    }

    obj.a    # should return 1
    obj.b.c  # should return 2

"""


class DictToObj(object):
    """Converts a Python dictionary into an object. Taking the dict as a contructor argument"""
    def __init__(self, **dictionary):
        self.add_dict(**dictionary)

    def add_dict(self, **dictionary):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                self.__dict__[key] = DictToObj(**value)
            else:
                self.__dict__[key] = value
    def __getitem__(self, key):
            return getattr(self, key)
