class Solution {
    public int numOfSubarrays(int[] arr) {
        // ArrayList<Integer> prifix = new ArrayList<>();
        // prifix.add(0);
        final long MOD = 1000000007L;
        int prifix=0;

        int odd_count=0;
        int even_count=1;
        int result=0;
        for (int x : arr){
            // prifix.add(prifix.get(prifix.size()-1)+x);
            prifix+=x;
            if (prifix%2!=0){
                odd_count+=1;
                result+=even_count;
            } else{
                even_count+=1;
                result+=odd_count;
            }
            result%=MOD;
        }
        System.out.println(result);

        return result;
    }
}