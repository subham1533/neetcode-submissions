class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        officer=0
        cm=1
        k=1
        n=len(nums)
        while (cm<n):
            if nums[cm]==nums[cm-1]:
                cm+=1
                continue
            else:
                officer+=1
                nums[officer]=nums[cm]
                cm+=1
                k+=1
        return k
                

                
        