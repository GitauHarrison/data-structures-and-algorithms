import java.util.Scanner;

public class EqualSumSolution {
    public static void main(String[] args) {
        
        Scanner obj = new Scanner(System.in);
        System.out.println("Enter a number:");
        int num1 = obj.nextInt();
        int num2 = obj.nextInt();
        int num3 = obj.nextInt();
        hasEqualSum(num1, num2, num3);
        
    }
    public static void hasEqualSum(int num1, int num2, int num3) {
        if ((num1 + num2) == num3) {
            // return true;
             System.out.println("True");
        } else {
            // return false;2
            System.out.println("False");
        }
    }
}
