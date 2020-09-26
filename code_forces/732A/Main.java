import java.util.*;
import java.io.*;

     

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        InputReader in = new InputReader(inputStream);
        
        int k, r;

        k = in.nextInt();
        r = in.nextInt();

        getValue(k, r);

    }
     
    public static void getValue(int k, int r) {
        int temp = k;

        for(int i=1; i<=1000; i++) {
            temp*=i;
            if((temp-r) % 10 == 0 || temp%10 == 0) {
                System.out.println(i);
                break;
            }
            temp = k;
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