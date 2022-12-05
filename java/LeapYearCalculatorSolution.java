import java.util.Scanner;

public class LeapYearCalculatorSolution {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        System.out.println("Enter a year: ");
        int year = obj.nextInt();

        isLeapYear(year);
        
    }
    public static boolean isLeapYear(int year) {
        if (year >= 1 && year < 9999) {
            if (year % 4 == 0){
                if (year % 100 == 0) {
                    if (year % 400 == 0) {
                        return true;
                        //System.out.println(year + " is leap year");
                    } else {
                        return false;
                        //System.out.println(year + " is leap year");
                    }
                } else {
                    return true;
                    //System.out.println(year + " is leap year");
                }
            } else {
                return false;
                // System.out.println(year + " is NOT a leap year");
            }
        } else {
            return false;
            // System.out.println(year + " is NOT a leap year");
        }
    }
}
