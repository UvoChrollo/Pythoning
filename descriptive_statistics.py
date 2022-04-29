from typing import List

class Desc:
    """
    Descriptive Statistics

    Available Function
    1. Mean
    2. Varians
    """

    def __init__(self, *nums):
        self.nums = nums
        self.len = len(nums)

    def mean(self):
        """
        >>> p1 = Desc(1,2,3)
        >>> print(p1.mean())
        2.0
        """
        return sum(self.nums) / self.len

    def variance(self):
        """
        >>> p1 = Desc(1,2,3)
        >>> print(p1.variance())
        1.0
        """
        rt = Desc.mean(self.nums)
        li = [(nu - rt)**2 for num in self.nums]
        return sum(li) / self.len

if __name__ == '__main__':
    import doctest
    doctest.testmod()