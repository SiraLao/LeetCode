class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        op = []

        for id1,i in enumerate(nums):
            for id2,j in enumerate(nums):
                if id1!=id2 and i + j == target:
                    op = [id1,id2]
                    break

        return op