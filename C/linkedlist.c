#include <stdio.h>
#include <stdlib.h>

struct Node{
    int data;
    struct Node *next;
} *HEAD=NULL;

int main(){
    struct Node *PTR, *NEW;
    char ch;
    int i=0;
    NEW = (struct Node *)malloc(sizeof(struct Node));
    printf("Enter value: ");
    scanf("%d", &NEW->data);
    NEW->next = NULL;
    HEAD = NEW;
    PTR = HEAD;
    fflush(stdin);


    while(i!=1){
        printf("Do you want to add (Y/N): ");
        scanf("%c", &ch);
        if(ch=='Y' || ch=='y'){
            NEW = (struct Node *)malloc(sizeof(struct Node));
            printf("Enter next value: ");
            scanf("%d", &NEW->data);
            NEW->next=NULL;
            PTR->next=NEW;
            PTR = PTR->next;
            fflush(stdin);
        }
        else{
            i=1;
        }
    }
    
    PTR = HEAD;
    printf("Entered values:");
    while(PTR!=NULL){
        printf(" %d", PTR->data);
        PTR=PTR->next;
    }

    //HEAD =NEW;
    PTR = HEAD;
    printf("Entered values:");
    while(PTR!=NULL){
        printf(" %d", PTR->data);
        PTR=PTR->next;
    }

    return 0;
}