class Solution {
    public int maxArea(int[] heights) {
        int start = 0;
        int end = heights.length - 1;

        int maxArea = 0;

        while (start < end) {
            int minHeight = Math.min(heights[start], heights[end]);
            maxArea = Math.max(maxArea, (end-start) * minHeight);

            if (heights[start] <= heights[end]) {
                start++;
            } else {
                end--;
            }
        }

        return maxArea;
    }
}
