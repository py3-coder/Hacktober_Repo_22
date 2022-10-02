/*
Factorial Trailing Zeroes
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.



Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0


Constraints:

0 <= n <= 104
 */
package BasicProblems;

import java.util.Scanner;

public class TrailingZeroInFactorial {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int trailingZero = 0;
        for(int i = 5; i <= num; i *= 5){
            trailingZero = trailingZero + num / i;
        }
        System.out.println(trailingZero);
    }
}
