package BasicProblems;

import java.util.Scanner;

public class PowerOfA {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();
        int power = sc.nextInt();
        System.out.println(findPower(number, power));
    }
    static int findPower(int a , int b){
        int result = 1;

        if(b == 0){
            return 1;
        }
        while(b > 0){

            if((b & 1) != 0){
                result *= a;
            }
            a *= a;
            b >>= 1;
        }
        return result;
    }
}
