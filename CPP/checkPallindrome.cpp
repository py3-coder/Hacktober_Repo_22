 { Driver Code Starts
 #include <stdio.h>
 #include <stdlib.h>
 #include <iostream>
 #include <stack>
 using namespace std;
 /* Link list Node */
 struct Node {
   int data;
   struct Node *next;
   Node(int x) {
     data = x;
     next = NULL;
   }
 };




  // } Driver Code Ends


 class Solution{
   public:
     //Function to check whether the list is palindrome.
     Node *rev(Node *head){
         Node *prev=NULL;
         Node *curr=head;

         while(curr!=NULL){
             Node* nextptr=curr->next;

             curr->next=prev;

             prev=curr;
             curr=nextptr;
         }
         return prev;
     }

     bool isPalindrome(Node *head)
     {
         //Your code here
         if(head==NULL or head->next==NULL){
             return true;
         }

         Node *sp=head;
         Node *sl=head;

         while(sp!=NULL && sp->next!=NULL){
             sl=sl->next;
             sp=sp->next->next;
         }
         // sl->next=rev(sl->next);       

         Node *h1=head;
         Node *h2;
         if(sp!=NULL){
          sl->next=rev(sl->next);
          h2=sl->next;
         }
         else if(sp==NULL)
             {
                  sl=rev(sl);
                  h2=sl;
             }
         while(h2!=NULL){
             if(h1->data!=h2->data)
                 return false;
             h1=h1->next;
             h2=h2->next;
         }

         return true;
     }
 };



 // { Driver Code Starts.
 /* Driver program to test above function*/
 int main()
 {
   int T,i,n,l,firstdata;
     cin>>T;
     while(T--)
     {

         struct Node *head = NULL,  *tail = NULL;
         cin>>n;
         // taking first data of LL
         cin>>firstdata;
         head = new Node(firstdata);
         tail = head;
         // taking remaining data of LL
         for(i=1;i<n;i++)
         {
             cin>>l;
             tail->next = new Node(l);
             tail = tail->next;
         }
     Solution obj;
    	cout<<obj.isPalindrome(head)<<endl;
     }
     return 0;
 }

   // } Driver Code Ends
