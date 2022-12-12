/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode start = new ListNode(0);
        start.next = head;
        ListNode leftPointer = start;
        ListNode rightPointer = start;
        
        for (int i = 0; i < n; i++) {
            rightPointer = rightPointer.next;
        }
        
        while (rightPointer.next != null) {
            leftPointer = leftPointer.next;
            rightPointer = rightPointer.next;
        }
        
        leftPointer.next = leftPointer.next.next;
        
        return start.next;
    }
}