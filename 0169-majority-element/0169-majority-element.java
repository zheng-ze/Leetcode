class Solution {
    public int majorityElement(int[] nums) {
        // https://www.cs.utexas.edu/~moore/best-ideas/mjrty/
        int max = nums[0];
        int count = 1;
        for (int i = 1; i < nums.length; i++) {
            if (count == 0) {
                max = nums[i];
                count++;
            } else if (nums[i] == max) {
                count++;
            } else {
                count--;
            }
        }
        
        return max;
    }
}