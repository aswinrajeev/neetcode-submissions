class StockSpanner {

    List<Integer> stockVals;

    public StockSpanner() {
        stockVals = new ArrayList<Integer>();
    }
    
    public int next(int price) {
        int span = 1;
        for (int i = 1; i <= stockVals.size(); i++) {
            int val = stockVals.get(stockVals.size() - i);
            if (val > price) {
                break;
            }
            span ++;
        }
        stockVals.add(price);
        return span;
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.next(price);
 */