import java.util.*;
import java.io.*;
     

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        LinkedList<Boolean> checkList = new LinkedList<>();

        int t = in.nextInt();

        for(int i=0; i<t; i++) {
            int count = 0;
            int n = in.nextInt();
            String temp = in.next();
            char[] arr = temp.toCharArray();
            for(char s: arr) {
                if(s == '(') {
                    checkList.add(true);
                } else if(s == ')' && checkList.size() > 0) {
                    checkList.removeLast();
                } else if(s == ')' && checkList.size() == 0) {
                    count++;
                }
            }
            out.println(count);
            checkList.clear();
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