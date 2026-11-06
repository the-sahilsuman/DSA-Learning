import java.util.Arrays;

class Solution {
    public int[] countServers(int n, int[][] logs, int x, int[] queries) {
        // Sort logs by time in ascending order
        Arrays.sort(logs, (a, b) -> Integer.compare(a[1], b[1]));
        
        int q = queries.length;
        // Store queries along with their original indices
        int[][] sortedQueries = new int[q][2];
        for (int i = 0; i < q; i++) {
            sortedQueries[i][0] = queries[i];
            sortedQueries[i][1] = i; 
        }
        
        // Sort queries by time in ascending order
        Arrays.sort(sortedQueries, (a, b) -> Integer.compare(a[0], b[0]));
        
        int[] ans = new int[q];
        // Array to track the frequency of requests per server in the current window
        // Sized n + 1 assuming 1-indexed server IDs (1 to n)
        int[] freq = new int[n + 1]; 
        int activeServers = 0;
        
        int left = 0;
        int right = 0;
        
        for (int[] query : sortedQueries) {
            int time = query[0];
            int originalIndex = query[1];
            
            // Expand window: Add logs that occurred up to the current query's time
            while (right < logs.length && logs[right][1] <= time) {
                int serverId = logs[right][0];
                if (freq[serverId] == 0) {
                    activeServers++; // A new unique server received a request
                }
                freq[serverId]++;
                right++;
            }
            
            // Shrink window: Remove logs that fall outside the [time - x, time] window
            while (left < logs.length && logs[left][1] < time - x) {
                int serverId = logs[left][0];
                freq[serverId]--;
                if (freq[serverId] == 0) {
                    activeServers--; // Server no longer has any requests in the window
                }
                left++;
            }
            
            // Calculate servers that received 0 requests
            ans[originalIndex] = n - activeServers;
        }
        
        return ans;
    }
}