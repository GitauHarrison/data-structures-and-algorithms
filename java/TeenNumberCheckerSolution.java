import java.util.Scanner;


public class TeenNumberCheckerSolution {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        System.out.println("Enter a number:");
        int num1 = obj.nextInt();
        int num2 = obj.nextInt();
        int num3 = obj.nextInt();
        hasTeen(num1, num2, num3);
    }
    public static boolean hasTeen(int num1, int num2, int num3){
        return isTeen(num1) || isTeen(num2) || isTeen(num3);
    }
 
    public static boolean isTeen(int var){
        return (var >= 13 && var <= 19);
    }
}
