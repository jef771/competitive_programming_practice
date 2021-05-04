import java.util.*;
import java.io.*;
     

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);

        String s = in.next();
        String sub = "";
        int big = Integer.MIN_VALUE;
        int small = Integer.MAX_VALUE;
        String reset = " ";
        String ansBig = "";
        String ansSmall = "";
        int k = in.nextInt();

        for(int i=0; i<s.length(); i++) {

            if(i+k <= s.length()) {
                for(int j=i; j<(i+k); j++) {

                    sub+=s.charAt(j);

                }
                
            if(sub.length() == k) {
                int temp = reset.compareTo(sub);

                if(temp <= small) {

                    if(temp == small) {
                        int temp2 = sub.compareTo(ansSmall);

                        if(temp2 > 0) {
                            ansSmall = sub; 
                        }
                    } else {
                        ansSmall = sub;
                        small = temp;
                    }
                } if (temp >= big){
                    ansBig = sub;
                    big = temp;
                }
              
            }
            sub="";
            }
        }

        out.println(ansBig);
        out.println(ansSmall);
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