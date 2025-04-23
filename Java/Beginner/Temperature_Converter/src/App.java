import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        
        Scanner scanner = new Scanner(System.in);

        double temp;
        double newTemp;
        String unit;

        System.out.print("Enter the Temperature: ");
        temp = scanner.nextDouble();

        System.out.print("Convert to Celsius or Fahrenheit? (C or F): ");
        unit = scanner.next().toUpperCase();

        // System.out.println(temp);
        // System.out.println(unit);

        // (condtition) ? true : false;
        newTemp = (unit.equals("C")) ? ((temp - 32) * 5 / 9) : ((temp * 5 / 9) + 32);

        System.out.printf("Converted temp is: %.2f°", newTemp);

        scanner.close();

    }
}
