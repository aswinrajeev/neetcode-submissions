class Solution {
    public int lengthOfLongestSubstring(String s) {

        Set<Character> charSet = new HashSet<>();
        int l = 0;
        int maxLen = 0;
        for (int r = 0; r < s.length(); r++) {
            char c = s.charAt(r);
            while (charSet.contains(c)) {
                charSet.remove(s.charAt(l));
                l++;
            }

            charSet.add(c);
            maxLen = Math.max(maxLen, (r-l) + 1);
        }

        return maxLen;
    }
}
