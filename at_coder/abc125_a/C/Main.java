import java.util.*;
import java.io.*;
     

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);

        int N; int ans = 0; int ans2 = 0;
        ArrayList<Integer> blackboard = new ArrayList<>();
        
        N = in.nextInt();
        for(int i=0; i<N; i++) {

            int temp = in.nextInt();
            blackboard.add(temp);
        }

        ans = getGCD(blackboard.get(0), blackboard.get(1));
        for(int i=2; i<N; i++) {
            ans2 = getGCD(ans, blackboard.get(i));
            System.out.println(ans2);
        }


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