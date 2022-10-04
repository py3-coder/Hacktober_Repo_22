#include<iostream.h>                
#include<conio.h>
void main()
{
clrscr();
char ch,c;
int cha;
cout<<“Enter a character:”;
cin>>ch;
cha=ch;
cout<<“nASCII value of “<<ch<<” is “<<cha;
c=ch+1; cha=c;
cout<<“nAdding one to the character:”<<“nASCII value of “<<c<<” is “<<cha;
getch();
}
