// Create java program for counting the number of words from the inserted sentence .
//sumit-awasthi->https://github.com/sumit-awasthi
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class CountOfWords {
       public static void main(String[] args) {
              Scanner sc = new Scanner(System.in);
              int c=0,w=0;
              String sentence=sc.nextLine();
              sentence = sentence.replace(",", " ");
              sentence = sentence.replace(";", " ");
              sentence = sentence.replace(":", " ");
              sentence = sentence.replace(".", " ");
              sentence = sentence.replace("?", " ");
              sentence = sentence.replace("!", " ");
              sentence=sentence.toLowerCase();
              String[] cwords=sentence.split(" ");
              HashMap<String,Integer> hm=new HashMap<String,Integer>();
              for(int i=0;i<cwords.length;i++)
              {
                     if(!cwords[i].equals(""))
                     {
                           w++;
                           if(hm.containsKey(cwords[i]))
                           {
                                  hm.replace(cwords[i],hm.get(cwords[i])+1);
                           }
                           else
                           {
                                  hm.put(cwords[i],1);
                           }
                     }
              }
              System.out.println("Number of words "+w);
              TreeMap<String,Integer> tm=new TreeMap<String,Integer>();
              tm.putAll(hm);
              System.out.println("Words with the count");
              for(Map.Entry element:tm.entrySet())
              {
                     System.out.println(element.getKey()+": "+element.getValue());
              }
              
       }
}
