class Solution {
    private int minimal_factor(long n){
        // if (n==1) return 1;
        if (n%2==0) return 2;
        if (n%3==0) return 3;
        for (int i=5;i*i<n;i+=6){
            if (n%i== 0) return (int) i;
            if (n%(i+2) == 0) return (int) (i + 2);
        }
        return (int) n;
    }
    public long minimumMaxValue(int n, int index, int value) {
        if (value==1) return -1;

        if (index > 0) {
            long prev = value;
            prev -= minimal_factor(prev);
            
            prev -= 2L * (index - 1);
            
            if (prev <= 0) {
                return -1;
            }
        }
        
        long curr = value;
        int remainingForwardSteps = n - 1 - index;
        
        if (remainingForwardSteps > 0) {
            curr += minimal_factor(curr);
            
            curr += 2L * (remainingForwardSteps - 1);
        }

        return curr;



        // long prev=value;
        // for (int i=index-1;i>=0;i--){
        //     int factor=minimal_factor(value);
        //     prev-=factor;
        //     if (prev <= 0) {
        //         return -1;
        //     }
        // }

        // int curr=value;
        // for (int j=index+1;j<n;j++){
        //     int factor1=minimal_factor(value);
        //     curr+=factor1;
        // }

        // return curr;

    }
}