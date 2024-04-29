import java.util.*;
import java.io.*;
     

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
       	
       	int[][] sheet=new int[3][3];
       	int[][] sheet2=new int[3][3];

       	for(int i=0;i<3;i++) {
       		for(int j=0;j<3;j++){
       			sheet[i][j]=in.nextInt();
       			sheet2[i][j]=0;
       		}
       	}

       	int N=in.nextInt();
       	boolean flag = false;

       	while(N-->0) {
       		int x=in.nextInt();

       		for(int i=0;i<3;i++) {
       			for(int j=0;j<3;j++){
       				if(sheet[i][j]==x) {
       					sheet2[i][j]=1;
       					boolean ans1 = check1(sheet2);
       					boolean ans2 = check2(sheet2);
       					boolean ans3 = check3(sheet2);
       					if(ans1 || ans2 || ans3) {
       						out.print("Yes");
       						out.close();
       						return;
       					}
       				}
       			}
       		}
       	}

       	out.print("No");
       	out.close();

    }

    static boolean check1(int[][] sheet) {
    	
    	for(int i=0;i<3;i++) {
    		int count=0;
       		for(int j=0;j<3;j++){
       			if(sheet[i][j]==1){
       				count++;
       			}
       			if(count==3) {
       				return true;
       			}
       		}		
       	}

       	return false;
    }

    static boolean check2(int[][] sheet) {
       	return (sheet[0][0] == 1 && sheet[1][1] == 1 && sheet[2][2] == 1) || 
       			(sheet[0][2] == 1 && sheet[1][1] == 1 && sheet[2][0] == 1);
    }

    static boolean check3(int[][] sheet) {
    	
    	for(int i=0;i<3;i++) {
    		int count=0;
       		for(int j=0;j<3;j++){
       			if(sheet[j][i]==1){
       				count++;
       			}
       			if(count==3) {
       				return true;
       			}
       		}		
       	}
       	return false;
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
