import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    private List<Integer> primeFactors(int x) {
        List<Integer> factors = new ArrayList<>();
        for (int d = 2; (long) d * d <= x; d++) {
            if (x % d == 0) {
                factors.add(d);
                while (x % d == 0) {
                    x /= d;
                }
            }
        }
        if (x > 1) {
            factors.add(x);
        }
        return factors;
    }

    private boolean hasConflict(List<Integer> pfRight, Set<Integer> activePrimes) {
        for (int p : pfRight) {
            if (activePrimes.contains(p)) {
                return true;
            }
        }
        return false;
    }

    public int maxLength(int[] nums) {
        int n = nums.length;
        if (n <= 1) {
            return n;
        }

        Set<Integer> activePrimes = new HashSet<>();
        int left = 0;
        int best = 1;

        for (int right = 0; right < n; right++) {
            List<Integer> pfRight = primeFactors(nums[right]);

            while (hasConflict(pfRight, activePrimes)) {
                for (int p : primeFactors(nums[left])) {
                    activePrimes.remove(p);
                }
                left++;
            }

            activePrimes.addAll(pfRight);
            best = Math.max(best, right - left + 1);
        }

        return Math.max(best, 2);
    }
}