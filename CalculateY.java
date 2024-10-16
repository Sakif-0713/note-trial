import java.util.Scanner;

public class CalculateY {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("The value of N: ");
        int N = scanner.nextInt();

        int y = 0;
        for (int i = 1; i <= N; i++) {
            int sum = 0;
            for (int j = 1; j <= i; j++) {
                sum += j;
            }
            y -= sum;
        }

        System.out.println("The value of y is: " + y);

        scanner.close();
    }
}
