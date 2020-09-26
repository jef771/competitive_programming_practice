import java.util.*;
import java.io.*;
     

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);

        String card = in.next();
        String hand[] = new String[5];


        for(int i=0; i<5; i++) {
            String temp = in.next();
            hand[i] = temp;
        }

        System.out.println(checkHand(hand, card));

    }

    public static String checkHand(String[] hand, String card) {
        String cardTwo[] = card.split("");

        for(String s: hand) {
            String temp[] = s.split("");
            if(temp[0].equals(cardTwo[0]) || temp[1].equals(cardTwo[1])) {
                return "YES";
            }
        }

        return "NO"; 
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
    }
}