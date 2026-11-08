class Solution {
    public int countServers(int[][] grid) {
        int m = grid.length;
        int n=grid[0].length;
        int[] rows= new int[m];
        int[] columns=new int[n];

        for(int i=0;i<m;i++){
            for (int j=0;j<n;j++){
                if (grid[i][j]==1){
                    rows[i]+=1;
                    columns[j]+=1;
                }
            }
        }

        int count=0;
        for(int i=0;i<m;i+=1){
            for (int j=0;j<n;j+=1){
                if (grid[i][j]==1 && (rows[i]>1 || columns[j]>1)){
                    count+=1;
                }
            }
        }

        return count;


    }
}