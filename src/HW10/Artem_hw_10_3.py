class Input(Exception):
    """
    Exception class
    """
    def __init__(self, const: int):
        """

        :param const: int
        """
        self.const = const


try:
    inp = input("Number: ")
    if not inp.isdigit():
        raise TypeError('pls enter number')
    else:
        print(f'your number is {inp}')
except Exception as error:
    print(error)
