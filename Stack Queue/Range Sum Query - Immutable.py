class NumArray:

    def __init__(self, nums: List[int]):
        self.cum = [0] + list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.cum[right+1] - self.cum[left]
