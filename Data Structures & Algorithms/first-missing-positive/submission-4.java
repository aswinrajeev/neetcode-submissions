class Solution {
    public int firstMissingPositive(int[] nums) {

        int len = nums.length;

        int i = 0;
        while (i < len) {
            if (nums[i] <= 0 || nums[i] > len) {
                i++;
                continue;
            }

            int index = nums[i] - 1;
            if (nums[index] != nums[i]) {
                int temp = nums[index];
                nums[index] = nums[i];
                nums[i] = temp;
            } else {
                i++;
            }
        }

        for (i = 0; i < len; i++) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }

        return len + 1;

    }
}