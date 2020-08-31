import java.util.*;
import java.io.*;

public class A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int ans = 0;
        int[][] arr = new int[n][3];

        for(int i=0; i<n; i++) {
            for(int j=0; j<3; j++) {
                int temp = sc.nextInt();
                arr[i][j] = temp; 
            }
        }

        for(int j=0; j<3; j++) {
            for(int i=0; i<n; i++) {
                ans+=arr[i][j];
            }
            if(ans != 0) {
                System.out.println("NO");
                System.exit(0);
            }
            ans = 0;
        }
        System.out.println("YES");
    }
}