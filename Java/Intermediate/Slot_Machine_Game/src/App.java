import java.util.Random;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {

        // SLOTS MACHINE GAME

        // DECLARE VARIABLES
        Scanner scanner = new Scanner(System.in);
        int balance = 100;
        int bet;
        int payout;
        String[] row;
        String playAgain;


        // DISPLAY WELCOME MESSAGE
        System.out.println("**************************");
        System.out.println("  Welcome to Java Slots");
        // System.out.println("Symbols: 🍒🍉🍋🔔⭐");
        System.out.println("Symbols: C, WM, L, B, S");
        System.out.println("**************************");

        // PLAY IF BALANCE > 0
        while(balance > 0){
            // ENTER BET AMOUNT
            System.out.println("Current Balance: $" + balance);
            System.out.println("Place your bet amount: ");
            bet = scanner.nextInt();
            scanner.nextLine(); // to clear the input buffer to remove \n character

            // VERIFY IF BET > BALANCE
            if(bet > balance){
                System.out.println("INSUFFICIENT FOUNDS");
                continue;
            }
            else if(bet <= 0){
                // VERIFY IF BET > 0
                System.out.println("Bet must be greater than 0");
                continue;
            }
            else{
                // SUBTRACT BET FROM BALANCE
                balance -= bet;
                // System.out.println("$" + balance);
            }

            // SPIN ROW
            System.out.println("Spinning...");
            row = spinRow();
            printRow(row);
            payout = getPayout(row, bet);

            if(payout > 0){
                System.out.println("You won $" + payout);
                balance += payout;
            }
            else{
                System.out.println("Sorry you lost this round");
            }

            System.out.print("Do you want to play again? (Y/N): ");
            playAgain = scanner.nextLine().toUpperCase();

            if(!playAgain.equals("Y")){
                break;
            }

        }

        // PRINT ROW

        // GET PAYOUT

        // ASK TO PLAY AGAIN

        // DISPLAY MESSAGE

        System.out.println("GAME OVER! Your final balance is: $" + balance);

        scanner.close();

    }

    // SPIN ROW - method declearation
    static String[] spinRow(){

        String[] symbols = {"C", "WM", "L", "B", "S"};
        String[] row = new String[3];
        Random random = new Random();

        // System.out.println(symbols[1]);

        // System.out.println(symbols[random.nextInt(symbols.length)]);

        for(int i = 0; i < 3; i++){
            row[i] = symbols[random.nextInt(symbols.length)];
        }

        // System.out.println(row[0] + " " + row[1] + " " + row[2]);

        return row;
    }

    static void printRow(String[] row){

        System.out.println("**************");
        System.out.println(" " + String.join(" | ", row));
        System.out.println("**************");
    }

    static int getPayout(String[] row, int bet){

        if(row[0].equals(row[1]) && row[1].equals(row[2])){
            return switch(row[0]){
                case "C" -> bet * 3;
                case "WM" -> bet * 4;
                case "L" -> bet * 5;
                case "B" -> bet * 10;
                case "S" -> bet * 20;
                default -> 0;
            };
        }
        else if(row[0].equals(row[1])){
            return switch(row[0]){
                case "C" -> bet * 2;
                case "WM" -> bet * 3;
                case "L" -> bet * 4;
                case "B" -> bet * 5;
                case "S" -> bet * 10;
                default -> 0;
            };
        }
        else if(row[1].equals(row[2])){
            return switch(row[1]){
                case "C" -> bet * 2;
                case "WM" -> bet * 3;
                case "L" -> bet * 4;
                case "B" -> bet * 5;
                case "S" -> bet * 10;
                default -> 0;
            };
        }

        return 0;
    }


}
