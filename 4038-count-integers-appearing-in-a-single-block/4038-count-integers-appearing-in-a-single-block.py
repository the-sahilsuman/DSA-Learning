class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        freq={}
        diff=set()
        for i,x in enumerate(nums):
            if x in diff:
                continue
            if x in freq:
                if (freq[x][0]+freq[x][1])==i:
                    freq[x][1]+=1
                else:
                    del freq[x]
                    diff.add(x)
            else:
                freq[x]=[i,1]

        return len(freq)

