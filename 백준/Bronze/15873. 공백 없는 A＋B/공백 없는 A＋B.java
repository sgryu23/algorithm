import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        if (num % 10 == 0) {
            num /= 100;
            System.out.println(10 + num);
        } else {
            int val = num % 10;
            num /= 10;
            if (num == 10) {
                System.out.println(10 + val);
            } else {
                System.out.println(val + num);
            }
        }
    }
}