class Solution {
    public int minMoves2(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        int median = nums[nums.length / 2];


        int count=0;

        for (int x:nums){
            count+=Math.abs(x-median);
        }

        return count;

    }
}