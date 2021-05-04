import java.util.*;
import java.io.*;

class A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next().toUpperCase();
        String b = sc.next().toUpperCase();

        char[] a1 = a.toCharArray();
        char[] b1 = b.toCharArray();
        char temp = a1[1];
        int x=0;

        if(a.length() > b.length || b.length > a.length) {
            return false;
        }

        for(int i=0; i<a1.length; i++) {
            for(int j=0; j<a1.length - 1; j++) {
                if(a1[j] > a1[j+1]) {
                    temp = a1[j+1];
                    a1[j+1] = a1[j];
                    a1[j] = temp;
                }if(b1[j] > b1[j+1]) {
                    temp = b1[j+1];
                    b1[j+1] = b1[j];
                    b1[j] = temp; 
                }
            }
        }
        for(int i=0; i<a1.length; i++) {
            if(a1[i] == b1[i]){
                x+=1;
            }
            System.out.println(a1[i]);
            System.out.println(b1[i]);
        }

        if(x == a.length()) {
            System.out.println("True");;
        } else {
            System.out.println("False");
        }

/*        char[] a1 = a.toCharArray();
        char[] b1 = b.toCharArray();

        Arrays.sort(a1);
        Arrays.sort(b1);

        String temp = new String();
        String temp2 = new String();

        for(int i=0; i<a1.length; i++) {
            temp+=a1[i];
            temp2+=b1[i];
        }

        boolean ans = temp.equals(temp2);

        if(ans == true) {
            System.out.println("Anagrams");
        } else {
            System.out.println("Not Anagrams");
        }*/
    }
}