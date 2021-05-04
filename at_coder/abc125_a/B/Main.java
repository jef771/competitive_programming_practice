import java.util.*;
import java.io.*;
     

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);

        int N; int ans = 0;
        ArrayList<Integer> V = new ArrayList<>();
        ArrayList<Integer> C = new ArrayList<>();

        N = in.nextInt();

        for(int i=0; i<N; i++) {
            int temp = in.nextInt();
            V.add(temp);
        }

        for(int i=0; i<N; i++) {
            int temp = in.nextInt();
            C.add(temp);
        }

        for(int i=0; i<N; i++) {
            if(V.get(i) - C.get(i) > 0) {
                ans+=(V.get(i)-C.get(i));
            }
        }

        System.out.print(ans);
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