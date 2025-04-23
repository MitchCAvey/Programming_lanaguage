import java.util.Random;

public class App {
    public static void main(String[] args) throws Exception {
        
        Random random = new Random();

        /*
        // Example using Integers
        int number1;
        int number2;
        int number3;


        // number = random.nextInt(); // This will generate a random number between -2Billion to +2Billion
        number1 = random.nextInt(1, 7); // set a range like so
        number2 = random.nextInt(1, 7);
        number3 = random.nextInt(1, 7);

        System.out.println("Die 1: " + number1 + "\nDie 2: " + number2 + "\nDie 3: " + number3);

        */

        /* 
        // Example using Doubles
        double number4;

        number4 = random.nextDouble(1, 7); // Generates a number between 0 and 0.9999...etc.

        System.out.println(number4);

        */

        // Example using Booleans

        boolean isHeads;

        isHeads = random.nextBoolean();

        // System.out.println(isHeads);

        if(isHeads){
            System.out.println("HEADS");
        }
        else{
            System.out.println("TAILS");
        }

    }
}
