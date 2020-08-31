import java.util.*;
import java.io.*;

public class A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String players = sc.nextLine();

        char[] line = players.toCharArray();

        int ans1 = 0;
        int ans2 = 0;
        for(char x: line) {
            if(ans1 == 7 || ans2 == 7) {
                break;
            }
            if(x == '1') {
                ans1++;
                ans2 = 0;
            } else {
                ans2++;
                ans1 = 0;
            }
        }

        if(ans1 == 7 || ans2 == 7) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}