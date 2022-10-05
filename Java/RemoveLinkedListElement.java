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
    public ListNode removeElements(ListNode head, int val) {
        if(head == null)
            return null;
        
        ListNode temp = head;
        while(temp.val == val) {
            temp = temp.next;
            if(temp == null)
                return null;
        }
        
        ListNode prev = temp;
        ListNode curr = temp.next;
        
        while(curr != null) {
            if(curr.val == val)
                prev.next = curr.next;
            else
                prev = curr;
            
            curr = curr.next;
        }
        return temp;
    }
}
