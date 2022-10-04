/*
Palindrome Number.
Given a number n. n is an integer.Check whether the n is palindrome or not
Example:
121 is a palindrome Number.
123 is not a palindrome Number.
*/

package BasicProblems;

import java.util.Scanner;

public class PalindromeNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int rev = 0;
        while(num > 0){
            int rem = num % 10;
            rev = rev * 10 +rem;
            num /= 10;
        }
        if(rev == num){
            System.out.println("Is Palindrome Number");
        }else{
            System.out.println("Not A Palindrome Number");
        }
    }
}
