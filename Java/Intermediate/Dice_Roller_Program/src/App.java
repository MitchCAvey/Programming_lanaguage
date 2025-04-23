import java.util.Random;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        
        // JAVA DICE ROLLER PROGRAM

        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        // Step 1: DECLARE VARIABLES
        int numOfDice;
        int total = 0;

        // Step 2: GET # OF DICE FROM THE USER

        System.out.print("Enter # of dice to roll: ");
        numOfDice = scanner.nextInt();

        // Step 3: CHECK IF # OF DICE > 0
        if(numOfDice > 0){
            // System.out.println("You roll the dice");
            // Step 4: ROLL ALL THE DICE
            for(int i = 0; i < numOfDice; i++){
                // Step 5: GET THE SUM OF ALL DICE
                int roll = random.nextInt(1, 7);
                printDie(roll);
                System.out.println("You rolled: " + roll);
                total += roll;
            }

            System.out.println("Total: " + total);
        }
        else{
            System.out.println("# of dice must be greater than 0");
        }

        scanner.close();

    }

    // Step 6: DISPLAY ASCII OF DICE
    static void printDie(int roll){

        String dice1 = """
                 -------
                |       |
                |   ●   |
                |       |
                 -------
                """;

        String dice2 = """
                 -------
                |     ● |
                |       |
                | ●     |
                 -------
                """;

        String dice3 = """
                 -------
                |     ● |
                |   ●   |
                | ●     |
                 -------
                """;

        String dice4 = """
                 -------
                | ●   ● |
                |       |
                | ●   ● |
                 -------
                """;

        String dice5 = """
                 -------
                | ●   ● |
                |   ●   |
                | ●   ● |
                 -------
                """;

        String dice6 = """
                 -------
                | ●   ● |
                | ●   ● |
                | ●   ● |
                 -------
                """;
        
        // System.out.println(dice1);

        switch(roll){
            case 1 -> System.out.println(dice1);
            case 2 -> System.out.println(dice2);
            case 3 -> System.out.println(dice3);
            case 4 -> System.out.println(dice4);
            case 5 -> System.out.println(dice5);
            case 6 -> System.out.println(dice6);
            default -> System.out.println("INVALID ROLL");
        }

    }

}
