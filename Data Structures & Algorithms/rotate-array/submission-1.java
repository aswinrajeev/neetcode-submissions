class Solution {
    public void rotate(int[] nums, int k) {
        int len = nums.length;
        int[] numsCopy = Arrays.copyOf(nums, len);
        for (int i=0; i < len; i++) {
            int nextIndex = (i + k) % len;
            nums[nextIndex] = numsCopy[i];
        }
    }
}


/**
1,2,3,4,5,6,7,8,9
5,6,7,4,1,2,3,8,9 
**/