package BasicProblems;

import java.util.Scanner;

public class GcdOfNumber {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num1, num2;
        num1 = sc.nextInt();
        num2 = sc.nextInt();

        System.out.println(gcd(num1, num2));

    }

    static  int gcd(int a , int b){
        if(b == 0) return  a;
        return gcd(a, a % b );
    }
}
