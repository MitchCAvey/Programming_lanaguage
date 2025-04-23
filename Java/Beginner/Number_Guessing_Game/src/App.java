import java.util.Random;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {

        // NUMBER GUESSING GAME

        Random random = new Random();
        Scanner scanner = new Scanner(System.in);

        int guess;
        int attempts = 0;
        int min = 1;
        int max = 100;
        int randomNumber = random.nextInt(min, max + 1);

        // System.out.println(randomNumber);

        System.out.println("Number Guessing Game!");
        System.out.printf("Guess a number between %d - %d: ", min, max);

        do{
            System.out.print("Enter your guess: ");
            guess = scanner.nextInt();
            attempts++;

            if(guess < randomNumber){
                System.out.println("TOO LOW! Try again");
            }
            else if(guess > randomNumber){
                System.out.println("TOO HIGH! Try again");
            }
            else{
                System.out.println("CORRECT!! The number was " + randomNumber);
                System.out.println("# of attempts: " + attempts);
            }

        }while(guess != randomNumber);

        // System.out.println("You have Won!!!");

        scanner.close();

    }
}
