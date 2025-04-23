import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * Enums = (Enumerations) A special kind of class that represents a fixed set of constants.
         *         They improve code readbility and are easy to maintain.
         *         More efficient with switches when comparing Strings.
        */

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a day of the week: ");
        String response = scanner.nextLine().toUpperCase();

        try{
            // Day day = Day.SUNDAY;
            Day day = Day.valueOf(response);

            // System.out.println(day);
            // System.out.println(day.getDayNumber());

            switch(day){
                case MONDAY,
                     TUESDAY,
                     WENDESDAY,
                     THURSDAY,
                     FRIDAY -> System.out.println("It is a weekday");
                case SATURDAY, SUNDAY -> System.out.println("It is the weekend");            
            }

        }
        catch(IllegalArgumentException e){
            System.out.println("Please enter a valid day!");
        }

        scanner.close();

    }
}
