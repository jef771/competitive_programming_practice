import java.util.*;
import java.io.*;

class A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int x = sc.nextInt();
        int y = sc.nextInt();

        System.out.println(s.substring(x,y));
    }
}