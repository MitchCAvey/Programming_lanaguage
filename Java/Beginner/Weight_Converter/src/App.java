import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {

        // WEIGHT CONVERSION PROGRAM

        // Declare variables
        Scanner scanner = new Scanner(System.in);

        double weight;
        double newWeight;
        int choice;

        // Welcome Message
        System.out.println("Weight Coversion Program");
        System.out.println("1: Convert lbs to kgs");
        System.out.println("2: Covert kgs to lbs");

        // Prompt for user input/choice
        System.out.print("Choose an option: ");
        choice = scanner.nextInt();

        // System.out.println(choice);


        if(choice == 1){
            // Option 1 convert lbs to kgs
            System.out.print("Enter the weight in lbs: ");
            weight = scanner.nextDouble();
            newWeight = weight * 0.453592;
            // System.out.println("The new weight in kgs is: " + newWeight);
            System.out.printf("The new weight in kgs is: %.2f", newWeight);
        }
        else if(choice == 2){
            // Option 2 convert kgs to lbs
            System.out.print("Enter the weight in kgs: ");
            weight = scanner.nextDouble();
            newWeight = weight * 2.20462;
            // System.out.println("The new weight in kgs is: " + newWeight);
            System.out.printf("The new weight in lbs is: %.2f", newWeight);
        }
        else{
            System.out.println("That was not a valid choice!");
        }

        // else print not a valid choice

        scanner.close();
    }
}
