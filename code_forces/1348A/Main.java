import java.util.*;
import java.io.*;
     

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);

        int T = in.nextInt();

        for(int i=0; i<T; i++) {
            int n = in.nextInt();
            out.println(solve(n));
        }

        out.close();
    }


    public static long solve(int n) {
        long sum1 = 0;
        long sum2 = 0;
        boolean flag = false;

        if(n == 2) {
            return 2;
        }

        for(int i=1; i<=n; i++) {
            double temp = Math.pow(2, i);
            if(!flag) {
                sum1+=temp;
                if(i == n/2-1) {
                    flag = true;
                }
            } else {
                sum2+=temp;
                if(i == n-1) {
                    flag = false;
                }
            }
        }


        return Math.abs(sum2 - sum1);
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