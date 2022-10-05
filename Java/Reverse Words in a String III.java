// REVERSE WORDS OF SENTENCE
class Solution {
    public String reverseWords(String s) {
        StringBuilder output = new StringBuilder();
        String[] arr = s.split(" ");
        StringBuilder rev = new StringBuilder();
        for(String str : arr) {
            output.append(rev.append(str).reverse().toString()+" ");
            rev.setLength(0);
        }
        
        return output.toString().trim();
    }
}
