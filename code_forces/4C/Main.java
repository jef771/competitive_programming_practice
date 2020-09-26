import java.util.*;
import java.io.*;
     

public class Main {

    public static void main(String[] args) {
        InputStream inputStream = System.in;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(System.out);
        HashMap<String, Integer> database = new HashMap<> ();

        int q = in.nextInt();

        for(int i=0; i < q; i++) {
            String temp = in.next();
            if(database.get(temp)!=null) {
                database.replace(temp, database.get(temp) + 1);
                out.println(temp + (database.get(temp)));
            } else {
                out.println("OK");
                database.put(temp, 0);
            }
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