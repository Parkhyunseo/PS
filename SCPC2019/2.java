/*
You should use the standard input/output

in order to receive a score properly.

Do not use file input and output

Please be very careful. 
*/

import java.util.Scanner;
import java.util.Math;
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
		for(int test_case = 0; test_case < T; test_case++) {
		    int R, S, E;
		    
		    R = sc.nextInt();
		    S = sc.nextInt();
		    E = sc.nextInt();
		    
		    int N;
		    
		    N = sc.nextInt();
		    
		    double distance = 0;
		    int last_ri = S;
		    
		    for(int i = 0; i < N; i ++)
		    {
		        int li, ri, hi;
		        
		        li = sc.nextInt();
		        ri = sc.nextInt();
		        hi = sc.nextInt();
		        
		        distance += ri-li;
		        if(2*(hi-R) >  0)
		            distance += 2*(hi-R)
		        distance += li -last_ri - 2*R
		        if(hi < R)
		            distance += 2*Math.PI*R*Math.atan2(R-hi, R)
		        else
		            distance += Math.PI*R
		            
		        last_ri = ri
		    }
		    
		    distance += E -last_ri - R
		    distance += R
		    
		    Answer = distance
			// Answer = 0;
			/////////////////////////////////////////////////////////////////////////////////////////////
			/*
			   Implement your algorithm here.
			   The answer to the case will be stored in variable Answer.
			 */
			/////////////////////////////////////////////////////////////////////////////////////////////


			// Print the answer to standard output(screen).
			System.out.println("Case #"+(test_case+1));
			System.out.println(Answer);
		}
	}
}