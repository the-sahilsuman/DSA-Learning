class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        result=0
        if costBoth<(cost1+cost2):
            if need1>need2:
                result+=(costBoth*need2)
                need1-=need2
                need2=0
            elif need1==need2:
                return costBoth*(need1)
            else:
                result+=(costBoth*need1)
                need2-=need1
                need1=0
                

        return result+(need1*min(costBoth,cost1))+(need2*min(costBoth,cost2))