class Solution {
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> count = new HashMap<>();

        int l = 0;
        int maxFreq = 0;
        int res = 0;

        for (int r = 0; r < s.length(); r++) {
            char c = s.charAt(r);
            int charCount = count.getOrDefault(c, 0) + 1;
            count.put(c, charCount);
            maxFreq = Math.max(charCount, maxFreq);

            while ((r-l) + 1 - maxFreq > k) {
                count.put(s.charAt(l), count.get(s.charAt(l)) - 1);
                l++;
            }

            res = Math.max(res, r-l+1);

        }

        return res;
    }
}
