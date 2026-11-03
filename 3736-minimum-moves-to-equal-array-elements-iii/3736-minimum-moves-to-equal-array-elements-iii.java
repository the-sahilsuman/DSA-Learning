class Solution {
    public int minMoves(int[] nums) {
        int max_value=Arrays.stream(nums).max().getAsInt();
        int count=0;

        for (int x : nums){
            count+=(max_value-x);
        }
        return count;
    }
}