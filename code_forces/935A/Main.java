import java.util.*;
import java.io.*;
     

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        InputReader in = new InputReader(inputStream);

        int x = in.nextInt();

        if(x%2 == 0 && x != 2) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
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