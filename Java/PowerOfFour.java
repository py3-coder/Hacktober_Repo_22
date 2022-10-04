package BasicProblems;

import java.util.Scanner;

public class PowerOfFour {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double num = sc.nextDouble();

        if(Math.pow(num, 0.5) == 4){
            System.out.println("True");
        }else{
            System.out.println("False");
        }
    }
}
