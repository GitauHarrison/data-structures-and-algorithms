import java.util.Arrays;
import java.util.Scanner;

public class findMinSolution {
    public static void main(String[] args) {
        int[] returnedArray = readIntegers();
        System.out.println(Arrays.toString(returnedArray));

        int returnedMin = findMin(returnedArray);
        System.out.println("min = " + returnedMin);
    }

    private static int[] readIntegers() {
        // Get user input
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a list of integers, separated by commas: ");
        String input = scanner.nextLine();

        // Split the input using commas
        String[] splits = input.split(",");

        // Get list as an array of strings
        int[] values = new int[splits.length];

        // Parse the array to get integers
        for (int i = 0; i < splits.length; i++) {
            values[i] = Integer.parseInt(splits[i].trim()); // trim() removes any whitespaces around the input
        }

        return values;
    }

    private static int findMin(int[] array) {
        int min = Integer.MAX_VALUE;
        // Compare user input against a set max value
        for (int el : array) {
            if (el < min) {
                min = el;
            }
        }
        return min;
    }
}

// Alternatively,
// You may use Array.sort()
// Then return the first element