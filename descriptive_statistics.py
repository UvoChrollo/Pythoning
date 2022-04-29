from typing import List

class Desc:
    """
    Descriptive Statistics

    Available Function
    1. Mean
    """

    def __init__(self, *nums):
        self.nums = nums

    def mean(self):
        """
        >>> p1 = Desc(1,2,3)
        >>> print(p1.mean())
        2.0
        """
        return sum(self.nums) / len(self.nums)

if __name__ == '__main__':
    import doctest
    doctest.testmod()