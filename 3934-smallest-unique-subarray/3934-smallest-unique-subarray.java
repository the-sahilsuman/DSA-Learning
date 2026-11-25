import java.util.HashMap;
import java.util.Map;

class Solution {
    private static final long BASE1 = 911_382_323L;
    private static final long MOD1  = 1_000_000_007L;
    private static final long BASE2 = 972_663_749L;
    private static final long MOD2  = 1_000_000_009L;

    public int smallestUniqueSubarray(int[] nums) {
        int n = nums.length;
        if (n <= 1) {
            return n;
        }

        long minVal = nums[0];
        for (int x : nums) {
            if (x < minVal) {
                minVal = x;
            }
        }

        long[] shifted = new long[n];
        for (int i = 0; i < n; i++) {
            shifted[i] = (long) nums[i] - minVal + 1L;
        }

        long[] pow1 = new long[n + 1];
        long[] pow2 = new long[n + 1];
        pow1[0] = 1L;
        pow2[0] = 1L;
        for (int i = 1; i <= n; i++) {
            pow1[i] = (pow1[i - 1] * BASE1) % MOD1;
            pow2[i] = (pow2[i - 1] * BASE2) % MOD2;
        }

        int low = 1;
        int high = n;
        int ans = n;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (hasUniqueSubarray(shifted, mid, pow1, pow2)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return ans;
    }

    private boolean hasUniqueSubarray(long[] arr, int len, long[] pow1, long[] pow2) {
        int n = arr.length;
        long h1 = 0;
        long h2 = 0;

        for (int i = 0; i < len; i++) {
            h1 = (h1 * BASE1 + arr[i]) % MOD1;
            h2 = (h2 * BASE2 + arr[i]) % MOD2;
        }

        Map<Long, Integer> freq = new HashMap<>();
        long key = pack(h1, h2);
        freq.put(key, 1);

        long p1 = pow1[len - 1];
        long p2 = pow2[len - 1];

        for (int i = 1; i <= n - len; i++) {
            long rem1 = (arr[i - 1] % MOD1 * p1) % MOD1;
            h1 = (h1 - rem1 + MOD1) % MOD1;
            h1 = (h1 * BASE1 + arr[i + len - 1]) % MOD1;

            long rem2 = (arr[i - 1] % MOD2 * p2) % MOD2;
            h2 = (h2 - rem2 + MOD2) % MOD2;
            h2 = (h2 * BASE2 + arr[i + len - 1]) % MOD2;

            key = pack(h1, h2);
            freq.put(key, freq.getOrDefault(key, 0) + 1);
        }

        for (int count : freq.values()) {
            if (count == 1) {
                return true;
            }
        }
        return false;
    }

    private long pack(long h1, long h2) {
        return (h1 << 32) | (h2 & 0xFFFFFFFFL);
    }
}