class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer=[]
        for i in range(len(nums)):
            flag=0
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    answer.append(i)
                    answer.append(j)
                    flag=1
                    break
            if flag==1:
                break

        return answer
