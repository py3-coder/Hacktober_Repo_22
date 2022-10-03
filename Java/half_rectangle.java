package half_rectangle;

public class Half_rectangle {

	public static void main(String[] args) {
		int n = 5;
		

//		for (int i = n; i >= 1; i--) {
//			for (int j = 1; j <= i; j++) {
//				System.out.print("*");
//			}
//			System.out.println(" ");
//
//		}
//		System.out.println();

//		for (int i = n; i >= 1; i--) {
//			for (int j = 1; j < i; j++) {
//				System.out.print(" ");
//			}
//			for (int j = 0; j <= n - i; j++) {
//				System.out.print("*");
//			}
//			System.out.println();
//
//		}
		int index = 1;
		for(int i = 1; i<=n; i++) {
			for(int j = 1; j<=i; j++) {
				System.out.print(index++);
				System.out.print(" ");
			}
			
			
			System.out.println();
		}

	}

}
