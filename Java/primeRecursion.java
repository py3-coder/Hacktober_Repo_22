public class primeRecursion
{
	public static void main(String[] args) {
		printPrime(15000, 2);
	}
	public static void printPrime(int n, int m){
	    if(n==3){
	        System.out.println(n);
	        System.out.println(n-1);
	        return;
	    }
	    if(n==2){
	        System.out.println(n);
	        return;
	    }
	    if(n<m){
	        return;
	    }
	    checkPrime(m, (int)Math.sqrt(m), 2);
	    printPrime(n, m+1);
	}
	public static void checkPrime(int n, int m, int x){
	    if(m<x)
	        System.out.println(n);
	    if(n%x==0)
	        return;
	    checkPrime(n,m, x++);
	}
}
