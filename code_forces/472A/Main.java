import java.util.*;
import java.io.*;
     

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        InputReader in = new InputReader(inputStream);

        int n = in.nextInt();
        int x = 0;
        int y = n;

        while(true) {
            int temp = 0;
            x++;
            y--;
            if(solve(x)) {
                temp++;
            } if(solve(y)) {
                temp++;
            } if(temp == 2) {
                break;
            }
        }

            System.out.println(x + " " + y);
    }

    public static boolean solve(int x) {
        
        boolean flag = false;
        for(int i=2; i<x/2+1; i++) {
            if(x%i == 0) {
                flag = true;
            }
        }

        return flag;
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