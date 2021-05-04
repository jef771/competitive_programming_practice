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
            out.println(solve(a, b));
        }

        out.close();
    }
     

    public static int solve(int a, int b) {
        int ans;
        if(a > b) {
            ans = a - b;
            if(ans%2 == 0) {
                return 1;
            } else {
                return 2;
            }
        } else if(a < b) {
            ans = b - a;
            if(ans%2 == 0) {
                return 2;
            } else {
                return 1;
            }
        } else {
            return 0;
        }
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