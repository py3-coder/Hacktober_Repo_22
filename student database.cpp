#include<iostream>
using namespace std;

//Student Struct
struct student{
    int rollNo;
    string name;
    float marks;
    string residentOf;
};

//Function to display a particular student
void displayStudent(student stdRecord[],int i){
    cout<<stdRecord[i].rollNo<<" "<<stdRecord[i].name<<" "<<stdRecord[i].marks<<" "<<stdRecord[i].residentOf<<"\n";
}

//Function to display the current complete database
void displayList(student stdRecord[],int n){
    for(int i=0;i<n;i++){
        displayStudent(stdRecord,i);
    }
}

//Function to Swap two records
void swap(student stdRecord[],int l,int r){
    student temp;
    temp=stdRecord[l];
    stdRecord[l]=stdRecord[r];
    stdRecord[r]=temp;
}

//Sort and display according to Roll No.
void bubbleSort(student stdRecord[],int n){
    for (int i = 0; i < n - 1; i++){
        for (int j = 0; j < n - i - 1; j++){
            if (stdRecord[j].rollNo > stdRecord[j + 1].rollNo){
                swap(stdRecord,j,j+1);
            }
        }
    }
}

//Insertion Sorting the Record according to the name alphabetincally and display
void insertionSort(student stdRecord[], int n){
    for (int i = 1; i < n; i++){
        int j = i;
        while (j > 0 && stdRecord[j-1].name > stdRecord[j].name){
            swap(stdRecord,j,j-1);
            j-- ;
        }
    }
    displayList(stdRecord,n);
}

//Partition function for the quickSort
int partition(student stdRecord[],int si,int end){
	int Mark=stdRecord[si].marks;
	int cnt=si;
	for(int i=si+1;i<=end;i++){
		if(stdRecord[i].marks<Mark) cnt++; 
	}
	swap(stdRecord,si,cnt);
	int i=si,j=end;
	while(i!=cnt && j!=cnt){
		if(stdRecord[i].marks<Mark) i++;
		else if(stdRecord[j].marks>Mark) j--;
		else swap(stdRecord,i,j);
	}
	return cnt;
}

//Quick Sort the Record and display the first 10 toppers
 void quickSort(student stdRecord[],int si,int end){
    if(si>=end){
    	return;
    }
    int pv=partition(stdRecord,si,end);
    
    quickSort(stdRecord,si,pv-1);
    quickSort(stdRecord,pv+1,end);
}

//Linear Search to display students having SGPA in the given range
void linearSearch(student stdRecord[], int n){
    int l,r;
        cout<<"Enter Range of SGPA: \nleftSGPA rightSGPA: ";
        cin>>l>>r;
            
    for (int i = 0; i < n; i++){
        if (stdRecord[i].marks>=l && stdRecord[i].marks<=r){
            displayStudent(stdRecord,i);
        }
    }
}

//Binary Search and displaying Record of Student by its Name
void binarySearch(student stdRecord[],int n){
    insertionSort(stdRecord,n);
    
    string name;
        cout<<"Enter The Name To Find: \n";
        cin>>name;

    int l  = 0 , r = n - 1 ; 
    while (l<=r){
       int mid = l + (r - l )/2 ; 
       if(stdRecord[mid].name == name){
       		displayStudent(stdRecord,mid);
       		return;
       		}
       else if(stdRecord[mid].name > name) r =  mid -1 ;
       else if(stdRecord[mid].name < name) l = mid + 1 ;
       else cout<<"No Such Student Name Exists\n";
    }
}

int main(){
    int n;
    cout<<"How many Student's Data You want to store: ";
    cin>>n;
    student stdRecord[n];
    cout<<"Now systematically add data in order : RollNo Name Marks ResidentOf \n";
    for(int i=0;i<n;i++){
        cin>>stdRecord[i].rollNo>>stdRecord[i].name>>stdRecord[i].marks>>stdRecord[i].residentOf;
    }
    int inputChoice;
    cout<<"Now Enter Choice\n1 for Roll No. Wise Display \n2 for Alphabetically Display \n3 for First 10 Toppers \n4 for Enter SGPA Range to find Students \n5 for Enter Name to Search \n0 for Exit ;(\n";
    while(true){
        cin>>inputChoice;
             if(inputChoice==1) bubbleSort(stdRecord,n);
        else if(inputChoice==2) insertionSort(stdRecord,n);
        else if(inputChoice==3) {
        							quickSort(stdRecord,0,n-1);
        							if(n>=10){
        								displayList(stdRecord,10);
        							}else{
        								displayList(stdRecord,n);
        							}
        						}
        else if(inputChoice==4) linearSearch(stdRecord,n);
        else if(inputChoice==5) binarySearch(stdRecord,n);
        else if(inputChoice==0) {cout<<"Thank You :)";break;}
        else cout<<"Enter Input";
        }
}