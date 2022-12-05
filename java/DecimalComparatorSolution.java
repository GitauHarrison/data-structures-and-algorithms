import java.util.Scanner;


public class DecimalComparatorSolution {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        System.out.println(("Enter first decimal number:"));
        double num1 = obj.nextDouble();

        Scanner obj2 = new Scanner(System.in);
        System.out.println(("Enter second decimal number:"));
        double num2 = obj2.nextDouble();

        areEqualByThreeDecimalPlaces(num1, num2);
    }
    public static boolean areEqualByThreeDecimalPlaces(double num1, double num2) {

        if ((int) (num1 * 1000) == (int) (num2 * 1000)) {
            return true;
            // System.out.println(num1 + " and " + num2 + " = True");
        } else {
            return false;
            // System.out.println(num1 + " and " + num2 + " = False");
        }
    }
    
}
