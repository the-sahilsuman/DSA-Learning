class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        remd=[0,0,0]
        for x in stones:
            remd[x%3]+=1
        
        if remd[0]%2==0:
            return remd[1]>0 and remd[2]>0
        return abs(remd[1]-remd[2])>2

        # # total=sum(stones)
        # # # print(total)
        # # if total%3==0:
        # #     return not len(stones)&1
        # # else:
        # #     return False