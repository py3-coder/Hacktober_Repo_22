/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class LinkedListCycleDetection {
    public boolean hasCycle(ListNode head) {
      // will use 2 pointer method fast and slow
        ListNode fast = head;
        ListNode slow = head;
        while(fast != null && fast.next != null){
          // increament fast with double speed of slow 
            fast = fast.next.next;
            slow = slow.next;
          // if both points to same node then return true as cycle is present in linked list
            if(fast == slow) return true;
        }
        // if loop over and didn't returned true then no cycle return false
        return false;
    }
}
