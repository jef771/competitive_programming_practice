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
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            out.println(solve(a, b, n));
        }

        out.close();
    }


    public static int solve(int a, int b, int n) {
        int ans = 0;
        int count = 1;
        while(ans < n) {
            ans = Math.max(a, b) + Math.min(a, b);
            if(ans > n) {
                break;
            }
            if(a < b) {
                a+=b;
            } else {
                b+=a;
            }
            count++;
        }

        return count;
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