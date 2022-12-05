import java.util.Scanner;

public class BarkingDogSolution{
    public static void main(String[] args) {

        Scanner obj = new Scanner(System.in);
        System.out.println("Is the dog barking? (true) or (false)");
        boolean barking = obj.nextBoolean();

        Scanner time = new Scanner(System.in);
        System.out.println("What hour of the day?");
        int hourOfDay = time.nextInt();

        shouldWakeUp(barking, hourOfDay);
        //System.out.println("At 0" + hourOfDay + " hours the state of the dog barking was " + barking);
    }
    public static boolean shouldWakeUp (boolean barking, int hourOfDay) {
        if (barking == true && hourOfDay >= 0 && hourOfDay < 8) {
            return true;
            // System.out.println("True");
        } else  if (barking == true && hourOfDay > 22 && hourOfDay < 24) {
            return true;
            // System.out.println("True");
        } else {
            return false;
            // System.out.println("False");
        }
    }
}
