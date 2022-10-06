/*
91. Decode Ways
Medium
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
Given a string s containing only digits, return the number of ways to decode it.
The test cases are generated so that the answer fits in a 32-bit integer.
 
Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
 
Constraints:
1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
*/
class Solution {
    public int numDecodings(String s) {
        Map<Integer,Integer> memo = new HashMap<>();
        return Solve(s,0,memo);
        
    }
    public static int Solve(String s,int i,Map<Integer,Integer> memo){
        // Base Case for way 1
        if(i==s.length()){
            return 1;
        }
        // When ever we enconter 0 --> "01" = 0 , "102"=0 "120"=0  
        if(s.charAt(i)=='0'){
            return 0;
        }
        if(memo.containsKey(i)){
            return memo.get(i);
        }
        // Base Case for way 2
        if(i==s.length()-1) return 1;
        // focus on only single elememts
        int way1 = Solve(s,i+1,memo);
        // focus on pair element 
        int way2 =0;
        // pair only considered when it int value is lower than 27.
        if(Integer.parseInt(s.substring(i,i+2))<=26){
            way2 =Solve(s,i+2,memo);
        }
        memo.put(i,way1+way2);
        return way1+way2;
    }
}
