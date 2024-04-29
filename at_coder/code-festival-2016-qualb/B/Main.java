import java.util.*;
import java.io.*;
     

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);

        int N,A,B;
        N=in.nextInt();
        A=in.nextInt();
        B=in.nextInt();
        String S=in.next();
       	
       	int aCount=0;
       	int bCount=0;
       	for(int i=0;i<N;i++){
       		if(S.charAt(i) == 'a') {
       			if(checkA(aCount,A,B)) {
       				aCount++;
       				out.println("Yes");
       			} else {
       				out.println("No");
       			}
       		} else if(S.charAt(i) == 'b') {
       			if(checkB(i, aCount, bCount, A, B)) {
       				aCount++;
       				bCount++;
       				out.println("Yes");
       			} else {
       				out.println("No");
       			}
       		} else {
       			out.println("No");
       		}
       	}

       	out.close();
    }

    public static boolean checkA(int count, int A, int B){
    	return count < (A+B);
    }
    
    public static boolean checkB(int index, int count, int count2, int A, int B) {
    	return count < (A+B) && count2+1 <= B;
    }
     
    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;
     
        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }
     
        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }
     
        public int nextInt() {
                return Integer.parseInt(next());
        }

        public long nextLong() {
                return Long.parseLong(next());
        }

        public String nextLine() {
            String str = "";
            try {
                if(tokenizer.hasMoreTokens()) {
                    str = tokenizer.nextToken("\n");
                } else {
                    str = reader.readLine();
                }
            } catch(IOException e) {
                throw new RuntimeException(e);
            }
            return str;
        }
    }
}
