import java.util.*;
import java.io.*;

class A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        String B = new String();
        
        char[] s = A.toCharArray();
        int size = s.length;
        for(int i= size-1; i>=0; i--) {
            B+=s[i];
        }

        boolean ans = A.equals(B);

        if(ans == true) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}