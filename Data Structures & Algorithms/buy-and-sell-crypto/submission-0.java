class Solution {
    public int maxProfit(int[] prices) {

        int len = prices.length;

        int[] historic_min = new int[len];
        int[] future_max = new int[len];

        int last_min = 100;
        int next_max = 0;
        for (int i = 0; i < len; i++) {
            last_min = Math.min(last_min, prices[i]);
            next_max = Math.max(next_max, prices[len - 1 - i]);

            historic_min[i] = last_min;
            future_max[len - 1 - i] = next_max;
        }

        int best_value = -100;
        for (int i=0; i < len; i++) {
            best_value = Math.max(best_value, future_max[i] - historic_min[i]);
        }

        return best_value;
        
    }
}

// [7,1,5,3,6,4]

//hm: [7,1,1,1,1,1]
//fm: [7,6,6,6,6,4]
