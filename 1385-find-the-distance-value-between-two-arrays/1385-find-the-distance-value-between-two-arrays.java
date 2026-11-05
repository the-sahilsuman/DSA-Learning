class Solution {
    public int findTheDistanceValue(int[] arr1, int[] arr2, int d) {
        
        int count=0;
        for (int x:arr1){
            boolean status=true;
            for (int y:arr2){
                if (Math.abs(x-y)<=d){
                    status=false;
                    break;
                }
            }
            if (status)
                count+=1;
        }
        return count;
    }
}