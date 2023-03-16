public class NumberOfDaysInMonthSolution {
    public static void main(String[] args) {
        // Sample month: 10, sample year: 2040
        getDaysInMonth(10, 2040);
    }
    public static boolean isLeapYear(int year){
    
        return year >= 1 && year <= 9999 && (year % 4 == 0 && year % 100 != 0 || year % 400 == 0);
    }
    
    public static int getDaysInMonth(int month, int year){
        if(year < 1 || year > 9999) {
            //return -1;
            System.out.println(-1);
        }
        switch(month){
            case 1: case 3: case 5: case 7: case 8: case 10: case 12:
                // Months with 31 days
                return 31;
                // System.out.println(31);
            case 4: case 6: case 9: case 11:
                // Months with 30 days
                return 30;
                // System.out.println(30);
            case 2:
                // Check if year is a leap year
                // Return number of days depending on the year
                return isLeapYear(year) ? 29 : 28;
                // System.out.println(isLeapYear(year) ? 29 : 28);
            default:
                    return -1; 
                    // System.out.println(-1);
        }
    }

}
