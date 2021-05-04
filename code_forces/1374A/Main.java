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
            int x, y, n;
            x = in.nextInt();
            y = in.nextInt();
            n = in.nextInt();
            out.println(solve(x, y, n));
        }

        out.close();
    }


    public static int solve(int x, int y, int n) {
        n-=y;
        n/=x;
        int ans = x*n + y;

        return ans;
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