class Solution {
    public int trap(int[] height) {
        int len = height.length;

        int[] prefix = new int[len];
        int[] suffix = new int[len];

        int pref_max = 0;
        int suf_max = 0;
        for (int i=0; i < len; i++) {
            if (height[i] > pref_max) {
                pref_max = height[i];
            }
            prefix[i] = pref_max;

            if (height[len - 1 - i] > suf_max) {
                suf_max = height[len - 1 - i];
            }
            suffix[len - 1 - i] = suf_max;
        }

        int result = 0;
        for (int i=0; i < len; i++) {
            result += Math.min(prefix[i], suffix[i]) - height[i];
        }

        return result;
    }
}
