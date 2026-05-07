class Solution {
    public int firstMissingPositive(int[] nums) {

        Set<Integer> numbers = new HashSet<>();
        for (int num: nums) {
            numbers.add(num);
        }

        for (int i = 1; i < Math.pow(2,31); i++) {
            if (!numbers.contains(i)) {
                return i;
            }
        }

        return 0;
        
    }
}