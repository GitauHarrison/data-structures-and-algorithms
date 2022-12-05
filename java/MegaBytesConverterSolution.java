public class MegaBytesConverterSolution {
    public static void main(String[] args) {
        int kiloBytes = 2500;

        if (kiloBytes < 0) {
            System.out.println("Invalid Value");
        } else {
            printMegaBytesAndKiloBytes(kiloBytes);
        }
    }
    public static void printMegaBytesAndKiloBytes(int kiloBytes) {
        int MB = kiloBytes / 1024;
        int KB = kiloBytes - (MB * 1024);

        if (kiloBytes < 0) {
            System.out.println("Invalid Value");
        } else {
            System.out.println(kiloBytes + " KB = " + MB + " MB and " + KB + " KB" );
        }
    }
}
