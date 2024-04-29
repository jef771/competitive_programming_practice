import java.util.*;
import java.io.*;
     

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);

        int N=in.nextInt();

        int[] arr=new int[N];

        int max=0;
        for(int i=0;i<N;i++){
        	int x=in.nextInt();
        	arr[i]=x;
        	max=Math.max(x,max);
        }

        int ans=Integer.MAX_VALUE;
        for(int i=1;i<=max;i++){
        	int count=countAns(i,arr);
        	ans=Math.min(ans,count);
        }

        out.print(ans);
        out.close();
       
    }

    public static int countAns(int i, int[] arr){
    	int tempAns=0;
    	for(int j=0;j<arr.length;j++){
    		tempAns+=(Math.pow(arr[j]-i, 2));
    	}

    	return tempAns; 
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

        public long nextLong() {
                return Long.parseLong(next());
        }

        public String nextLine() {
            String str = "";
            try {
                if(tokenizer.hasMoreTokens()) {
                    str = tokenizer.nextToken("\n");
                } else {
                    str = reader.readLine();
                }
            } catch(IOException e) {
                throw new RuntimeException(e);
            }
            return str;
        }
    }
}
