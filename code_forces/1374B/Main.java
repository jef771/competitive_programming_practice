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
            int temp = in.nextInt();
            out.println(solve(temp));
        }

        out.close();
    }
     

    public static int solve(int n) {
        int ans = 0;
        while(n > 1) {
            ans++;
            if(n%6 == 0) {
                n/=6;
            } else {
                n*=2;
            }
        }

        if(n == 1) {
            return ans;
        } else {
            return -1;
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