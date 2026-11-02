class Solution {
    public int minMergedInteger(int[] nums) {
        int n=nums.length;
        int val= Integer.MAX_VALUE;

        for(int i=0;i<n;i+=2){
            String x=String.valueOf(nums[i])+String.valueOf(nums[i+1]);
            val=Math.min(Integer.parseInt(x),val);

        }

        return val;
    }
}