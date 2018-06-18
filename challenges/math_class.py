import numbers

"""
Implement a math class with methods for addition, subtraction,
multiplication and division. If an input is provided that is not an
int, a message should be returned instead of raising an error.

    'a' + 3  # should return 'Inputs must be numbers!'

"""


class Math:
    error_message = 'Inputs must be numbers!'
    
    def add(self, *args):
        sum = 0

        for arg in args:
            if isinstance(arg, numbers.Number):
                sum = sum + arg
            else:
                return self.error_message
        
        return sum

    def subtract(self, *args):
        difference = 0

        for arg in args:
            if isinstance(arg, numbers.Number):
                difference = arg if difference is 0 else difference - arg
            else:
                return self.error_message

        return difference
        
    def multiply(self, *args):
        product = 0

        for arg in args:
            if isinstance(arg, numbers.Number):
                product = arg if product is 0 else product * arg
            else:
                return self.error_message

        return product
    
    def divide(self, *args):
        quotient = 0

        for arg in args:
            if isinstance(arg, numbers.Number):
                quotient = arg if quotient is 0 else quotient / arg
            else:
                return self.error_message

        return quotient
