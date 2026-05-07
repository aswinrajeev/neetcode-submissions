class Solution {
    public int maxProfit(int[] prices) {

        int len = prices.length;

        int minBuyPrice = 100;
        int maxProfit = -100;

        for (int i=0; i< len; i++) {
            minBuyPrice = Math.min(minBuyPrice, prices[i]);
            maxProfit = Math.max(maxProfit, prices[i] - minBuyPrice);
        }

        return maxProfit;

    }
}