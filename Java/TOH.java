/*Tower of Hanoi is a mathematical puzzle where we have three rods (A, B, and C) and N disks. 
Initially, all the disks are stacked in decreasing value of diameter i.e., the smallest disk is placed on the top and they are on rod A. 
The objective of the puzzle is to move the entire stack to another rod (here considered C), obeying the following simple rules: 
        1-Only one disk can be moved at a time.
        2-Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved 
          if it is the uppermost disk on a stack.
        3-No disk may be placed on top of a smaller disk.
*/  
  
public class TOH {
	
	public static void towerHanoi(int n,char s,char h,char d) {
		if(n==1) {
			System.out.println("Move 1st disk from "+s+" to "+d);
			return;
		}
		
		towerHanoi(n-1, s, d, h);
		System.out.println("Move "+n+"th disk from "+s+" to "+d);
		towerHanoi(n-1, h, s, d);
	}

	public static void main(String[] args) {
		
		towerHanoi(4, 's','h','d');

	}

}
