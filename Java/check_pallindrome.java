package check_pallindrome;
import java.util.*;

public class CeckPalindrome {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter Number");
		int n = sc.nextInt();
		int sum = 0, r;
		int temp = n ;
		while(n>0) {
			r = n % 10;
			sum = (sum*10)+ r;
			n = n/10;
			
		}
		if(temp==sum) {
			System.out.println("This Number is palindrome");
		}
		else {
			System.out.println("This Number is not pakindrome");
		}
		
		

	}

}
