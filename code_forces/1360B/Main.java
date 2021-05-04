import java.util.*;
import java.io.*;
     

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        
        int t = in.nextInt();

        for(int i=0; i<t; i++) {
            int n = in.nextInt();
            Integer[] at = new Integer[n];
            for(int j=0; j<n; j++) {
                at[j] = in.nextInt();
            }
            Arrays.sort(at, Collections.reverseOrder());
            int minimum = Integer.MAX_VALUE;
            for(int k = 0; k<n; k++) {
                for(int l = 0; l<n; l++) {
                    if(k!=l) {
                        if(Math.abs(at[k] - at[l]) < minimum) {
                            minimum = Math.abs(at[k] - at[l]);
                        }
                    }
                }
            }
            out.println(minimum);
        }
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
    }
}