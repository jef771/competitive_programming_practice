import java.util.*;
import java.io.*;
     

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        InputReader in = new InputReader(inputStream);

        int k, l, m, n, d, ans = 0;

        k = in.nextInt();
        l = in.nextInt();
        m = in.nextInt();
        n = in.nextInt();
        d = in.nextInt();


        for(int i=1; i<=d; i++) {
            if(i%k == 0 || i%l == 0 || i%m == 0 || i%n == 0) {
                ans++;
            }
        }

        System.out.println(ans);
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