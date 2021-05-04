import java.util.*;
import java.io.*;
     

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);

        int t = in.nextInt(), even = 0, odd = 0, sum = 0;

        for(int i=0; i<t; i++) {
            int n = in.nextInt();
            for(int j=0; j<n; j++) {
                int temp = in.nextInt();
                sum+=temp;
                if(temp%2 == 0) {
                    even++;
                } else {
                    odd++;
                }
            }
            if(sum%2!=0) {
                out.println("YES");
            } else {
                if(even > 0 && odd > 0) {
                    out.println("YES");
                } else {
                    out.println("NO");
                }
            }
            sum*=0;
            even*=0;
            odd*=0;
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