import java.util.*;
import java.io.*;
     

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);

        int n = in.nextInt();
        int m = in.nextInt();

        int moves = 0;
        if(n%2==0) {
            moves = n/2;
            while(moves%m!=0) {
                moves++;
                if(moves > n) {
                    moves = -1;
                    break;
                }
            }
        } else {
            moves = (n-1)/2;
            moves+=1;
            while(moves%m!=0) {
                moves++;
                if(moves>n) {
                    moves = -1;
                    break;
                }
            }
        }

        System.out.println(moves);

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