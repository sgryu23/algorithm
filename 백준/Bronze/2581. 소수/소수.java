import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int M = Integer.parseInt(br.readLine());
        int N = Integer.parseInt(br.readLine());
        int min = N;
        int sum = 0;
        
        for(int i = M; i <= N; i++) {
            // 소수 판별
            boolean check = true;
            // 1은 소수가 아니므로 false로 저장
            if(i == 1) check = false;
            
            for(int j = 2; j < i; j++) {
                // 나누어 떨어지면 check에 false 저장하고 반복 종료
                if(i % j == 0) {
                    check = false;
                    break;
                }
            }
            
            // check가 true라면 소수니까 합하고 최솟값 저장
            if(check) {
                if(min > i) min = i;
                sum += i;
            }
        }
        if(sum == 0) {
            System.out.println(-1);
        } else {
            System.out.println(sum + "\n" + min);
        }
    }
}