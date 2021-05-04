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
            int a = in.nextInt();
            int b = in.nextInt();
            if(a > b) {
                out.println(solveA(a, b));
            } else if(b > a) {
                out.println(solveB(a, b));
            } else {
                out.println(0);
            }
        }

        out.close();
    }


    public static int solveA(int a, int b) {
        int temp = a - b;
        if(temp%10 == 0) {
            return (a - b) / 10;
        } else {
            return (a - b) / 10 + 1;
        }
    }

    public static int solveB(int a, int b) {
        int temp = b - a;
        if(temp%10 == 0) {
            return (b - a) / 10;
        } else {
            return (b - a) / 10 + 1;
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