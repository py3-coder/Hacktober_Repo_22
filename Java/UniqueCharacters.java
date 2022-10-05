// Username - Saurabh-2809
// Github Id - https://github.com/Saurabh-2809

import java.util.regex.*; 
import java.util.Scanner;
public class UniqueCharacters{
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter the sentence:");
        String sentence = s.nextLine();
        sentence = sentence.toLowerCase();
         if(!Pattern.matches("^[ A-Za-z]+$",sentence))
         {
             System.out.println("Invalid Sentence");
         }
         else{
             int[] count = new int[256]; 
             
             int i; 
        for (i = 0; i < sentence.length(); i++) 
            if(sentence.charAt(i)!=' ') 
                count[(int)sentence.charAt(i)]++; 
                int n = i; 
                int d=0;
        for (i = 0; i < n; i++) 
           {
               if (count[(int)sentence.charAt(i)] == 1) 
               {
                   d++;
                   break;
               }
           }  
       if(d==0)
       {
           System.out.print("No unique characters");
       }
     else{
         System.out.print("Unique characters:");
     
        for (i = 0; i < n; i++) 
            if (count[(int)sentence.charAt(i)] == 1) 
                System.out.print(sentence.charAt(i)+" ");
         }}      
    }
}
