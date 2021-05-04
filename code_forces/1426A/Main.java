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
            int x = in.nextInt();
            out.println(getFloor(n, x));
        }

        out.close();
    }


    public static int getFloor(int n, int x) {
        int ans = 2, count = 0;
        for(int i = 3; i<1001; i++, count++) {
            if(i == n) {
                if(count == x) {
                    ans++;
                    return ans;
                }
                return ans;
            } else {
                if(count == x) {
                    ans++;
                    count*=0;
                }
            }
        }

        return 1;
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