class Solution {
public Node copyRandomList(Node head) {

//creating a new (deep copy node) and connecting 1st original node to deep copy node
    // then deep copy node to 2nd original node so on... 
	
    Node iter=head;
    Node front=head;
    
    while(iter!=null){
        front=iter.next;
        Node copy=new Node(iter.val);
        iter.next=copy;
        copy.next=front;
        iter=front;
    }
    
    //connecting ramdom links
    
    iter=head;
    while(iter!=null){
        if(iter.random!=null)
        iter.next.random=iter.random.next; //imp
        iter=iter.next.next;      // iter moves to next original node
    }
    
    //segrigation of two lists
    iter=head;
    Node pseudo=new Node(0); //new node used for track of head to return the deep copy list
    Node copy=pseudo;
    
    while(iter!=null){
        front=iter.next.next;//iter moves to next original node
        copy.next=iter.next; //deep copy links to next deep copy
        iter.next=front;     // original node links to next original node
        copy=copy.next;      //copy pointer moves to next copy node
        iter=iter.next;      //iter pointer moves to next original node
    }
    
    return pseudo.next;

    
}
}
