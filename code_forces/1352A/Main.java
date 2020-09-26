import java.util.*;
import java.io.*;
     

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);

        int t = in.nextInt();
        int numbers[] = new int[t];
        ArrayList <Integer> ans = new ArrayList<>();

        for(int i=0; i<t; i++) {
            int temp = in.nextInt();
            numbers[i] = temp;
        }

        for(int x: numbers) {
            int size = 0;
            while(x > 0) {
                int temp = 0;
                temp = x%10;
                x/=10;
                ans.add(temp);
                if(temp != 0) {
                    size++;
                }
            }
            if(x!=0) {
                ans.add(x);
            }
            int y = 1;
            out.println(size);
            for(int i = 0; i<ans.size(); i++) {
                if(ans.get(i) != 0 ) {
                    out.print(ans.get(i)*y + " ");;                    
                }
                y*=10;
            }
            out.println("");
            ans.clear();
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