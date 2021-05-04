import java.util.*;
import java.io.*;
     

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);

        int N; int g; int g2;

        N = in.nextInt();

        for(int i=0; i<N; i++) {

            int temp = in.nextInt();
            g = (temp/2);
            g2 = 2*(temp/2);
            out.println(getGCD(g, g2));
        }
        

        out.close();
    }
     
    static int getGCD(int a, int b) {
        int R;
        while((a % b) > 0) {
            R = a%b;
            a = b;
            b = R;
        }

        return b;
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