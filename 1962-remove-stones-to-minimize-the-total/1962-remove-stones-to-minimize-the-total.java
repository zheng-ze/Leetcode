import java.util.PriorityQueue;

class Solution {
    public int minStoneSum(int[] piles, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(piles.length, Collections.reverseOrder());
        int total = 0;
        
        for (int pile : piles) {
            total += pile;
            pq.add(pile);
        }
        
        while (k-- > 0) {
            int temp = pq.poll();
            total -= temp / 2;
            pq.add(temp - temp / 2);
        }
        
        return total;
    }
}