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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode root = new ListNode();
        ListNode result = root;
        int val = 0;
        while(l1 != null || l2 != null || val > 0) {
            if(l1 != null) {
                val += l1.val;
                l1 = l1.next;
            }

            if(l2 != null) {
                val += l2.val;
                l2 =l2.next;
            }
            result.next = new ListNode(val % 10);
            result = result.next;
            val = val / 10;
        }

        return root.next;
    }
}