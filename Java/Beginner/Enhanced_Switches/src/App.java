import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {

        // Enhanced switch = A replacement to many else if statements
        //                   (Java14 features)

        Scanner scanner = new Scanner(System.in);

        // Example 1 - to many if else if statements

        // String day = "Saturday";

        // if(day.equals("Monday")){
        //     System.out.println("It is a weekday");
        // }
        // else if(day.equals("Tuesday")){
        //     System.out.println("It is a weekday");
        // }
        // else if(day.equals("Wednesday")){
        //     System.out.println("It is a weekday");
        // }
        // else if(day.equals("Thursday")){
        //     System.out.println("It is a weekday");
        // }
        // else if(day.equals("Friday")){
        //     System.out.println("It is a weekday");
        // }
        // else if(day.equals("Saturday")){
        //     System.out.println("It is the weekend");
        // }
        // else if(day.equals("Sunday")){
        //     System.out.println("It is the weekend");
        // }
        // else{
        //     System.out.printf("%s Is not a day!", day);
        // }

        // Example 2 
        /*
        String day = "Wednesday";

        switch(day){
            case "Monday" -> System.out.println("It is a weekday");
            case "Tuesday" -> System.out.println("It is a weekday");
            case "Wednesday" -> System.out.println("It is a weekday");
            case "Thursday" -> System.out.println("It is a weekday");
            case "Friday" -> System.out.println("It is a weekday");
            case "Saturday" -> System.out.println("It is the weekend");
            case "Sunday" -> System.out.println("It is the weekend");
            default -> System.out.printf("%s Is not a day!", day);
        }
        */

        // Example 3

        String day;

        System.out.print("Enter the day of the week: ");
        day = scanner.nextLine();

        switch(day){
            case "Monday", "Tuesday", "Wednesday", "Thursday", "Friday" -> System.out.println("It is a weekday"); 
            case "Saturday", "Sunday" -> System.out.println("It is the weekend");
            default -> System.out.printf("%s Is not a day!", day);
        }

        scanner.close();
    }
}
