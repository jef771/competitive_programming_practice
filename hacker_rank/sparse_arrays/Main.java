import java.util.*;
import java.io.*;
     

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);

        HashMap<String, Integer> words = new HashMap<>();
    
        int n, n2;

        n = in.nextInt();

        for(int i=0; i<n; i++) {

            String temp = in.next();
            if(words.get(temp)==null) {
                words.put(temp, 1);
            } else {
                words.replace(temp, words.get(temp)+1);
            }
        }

        n2 = in.nextInt();

        for(int i=0; i<n2; i++) {

            String temp = in.next();
            out.println(words.getOrDefault(temp, 0));
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