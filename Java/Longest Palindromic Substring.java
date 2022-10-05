class Solution {
    public String longestPalindrome(String s) {
        int n=s.length();
        boolean dp[][]=new boolean[n][n];
        
        for(int i=0;i<n;i++)
            dp[i][i]=true;
        
        String ans=""+s.charAt(0);
        
        for(int i=n-1;i>=0;i--)
        {
            for(int j=i+1;j<n;j++)
            {
                if(s.charAt(i)==s.charAt(j) && (j-i==1 || dp[i+1][j-1]))
                {
                    dp[i][j]=true;
                    
                    if(ans.length()<(j-i+1))
                        ans=s.substring(i,Math.min(j+1,n));
                }
            }
        }
        
        return ans;
    }
}