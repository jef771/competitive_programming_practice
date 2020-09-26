import java.util.*;
import java.io.*;

     

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        InputReader in = new InputReader(inputStream);

        int n, m;

        n = in.nextInt();
        m = in.nextInt();
        boolean flag = false;

        for(int i=1; i<=n; i++) {
            for(int j=0; j<m; j++) {
                if(i%2 != 0) {
                    System.out.print("#");
                } else {
                    if(!flag) {
                        printSnake(m, flag);
                        flag = true;
                        break;
                    } else {
                        printSnake(m, flag);
                        flag = false;
                        break;
                    }
                }
            }
            System.out.println("");
        }
    }

    public static void printSnake(int n, boolean flag) {
        for(int i=0; i<n; i++) {
            if(i == 0 && flag) {
                System.out.print("#");
            } else if (i == n-1 && !flag) {
                System.out.print("#");
            } else {
                System.out.print(".");
            }
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