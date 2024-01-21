import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        
        Scanner in = new Scanner(System.in);
        
        int A = in.nextInt();
        int B = in.nextInt();
        
        int C = in.nextInt();
        
        int minute = 60 * A + B;
        minute += C;
        
        int h = (minute / 60) % 24;
        int m = minute % 60;
        
        System.out.println(h + " " + m);
    }
}