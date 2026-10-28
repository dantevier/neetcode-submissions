class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        set_zero = {}
        result = [1] * len(nums)
        for idx, num in enumerate(nums):            
            if num == 0:
                set_zero[idx]=num
                result = [0] * len(nums)
                if len(set_zero) > 1:
                    return [0] * len(nums)
                continue
            else:
                total = num * total
        for idx, num in enumerate(nums):
            if num == 0:
                result[idx] = int(total)
            else:
                result[idx] = int(total / num) * result[idx]
        return result