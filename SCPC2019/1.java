/*
You should use the standard input/output

in order to receive a score properly.

Do not use file input and output

Please be very careful. 
*/

import java.util.Scanner;

/*
   As the name of the class should be Solution , using Solution.java as the filename is recommended.
   In any case, you can execute your program by running 'java Solution' command.
 */
class Solution {
	static int Answer;

	public static void main(String args[]) throws Exception	{
		/*
		   The method below means that the program will read from input.txt, instead of standard(keyboard) input.
		   To test your program, you may save input data in input.txt file,
		   and call below method to read from the file when using nextInt() method.
		   You may remove the comment symbols(//) in the below statement and use it.
		   But before submission, you must remove the freopen function or rewrite comment symbols(//).
		 */		

		/*
		   Make new scanner from standard input System.in, and read data.
		 */
		Scanner sc = new Scanner(System.in);
		//Scanner sc = new Scanner(new FileInputStream("input.txt"));

		int T = sc.nextInt();
		
					
        int[] dp = new int[100001];
			
		for(int i = 2 ; i <= 100000 ; i++)
		{
		    if(i % 2 == 0)
		        dp[i] = dp[i/2] + 1;
		    else
		        dp[i] = dp[(i+1)/2] + 2;
		}
		    
		for(int test_case = 0; test_case < T; test_case++) {

			Answer = 0;
			int n1, n2;
			
			n1 = sc.nextInt();
			n2 = sc.nextInt();

		
		    for(int n = n1; n <= n2; n++)
		    {
		        Answer += dp[n];
		    }
		    
			// Print the answer to standard output(screen).
			System.out.println("Case #"+(test_case+1));
			System.out.println(Answer);
		}
	}
}