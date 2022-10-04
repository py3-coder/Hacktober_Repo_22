package BasicProblems;

import java.util.Scanner;

public class Factorial {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int fact = 1;

        if(num == 0 || num == 1){
            System.out.println(1);
        }else{
            while(num > 0){
                fact *= num;
                num--;
            }

            System.out.println(fact);
        }

    }
}
