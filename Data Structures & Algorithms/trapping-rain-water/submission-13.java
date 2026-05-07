class Solution {
    public int trap(int[] height) {

        int mapSize = height.length;

        if (mapSize <= 1) {
            return 0; // No water can be stored.
        }

        int start = 0;                                      // 1                                  
        int end = mapSize - 1;                              // 4                          
        int waterStored = 0;                                // 0                         

        int leftMax = height[0];                            // 4                        
        int rightMax = height[mapSize - 1];                 // 5         

        while (start <= end) {
            leftMax = Math.max(leftMax, height[start]);     // 4
            rightMax = Math.max(rightMax, height[end]);     // 5
            
            int water;
            if (height[start] <= height[end]) {             // 0 < 2
                water = Math.min(leftMax, rightMax)         // 4                            
                            - height[start];
                start++;                                    // 3    
            } else {
                water = Math.min(leftMax, rightMax)
                            - height[end];
                end--;
            }

            if (water > 0) {
                waterStored += water;                       // 6
            }
        }

        return waterStored;
    }
}
