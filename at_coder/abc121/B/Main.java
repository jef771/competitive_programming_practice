import java.util.*;
import java.io.*;
     

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
       	
       	int N,M,C;
       	N=in.nextInt();
       	M=in.nextInt();
       	C=in.nextInt();

       	int[] arrB=new int[M];

       	for(int i=0;i<M;i++) {
       		arrB[i]=in.nextInt();
       	}

       	int[] arrA=new int[M];
       	int count=0;
       	while(N-->0) {
       		
       		for(int i=0;i<M;i++){
       			arrA[i]=in.nextInt();
       		}

       		int sum=0;
       		for(int i=0;i<M;i++) {
       			sum+=((arrA[i])*(arrB[i]));
       		}
       		
       		sum+=C;
       		if(sum > 0) {
       			count++;
       		}	
       	}
       	
       	out.print(count);
       	out.close();
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
