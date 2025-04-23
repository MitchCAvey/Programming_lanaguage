import java.util.InputMismatchException;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * Exception = An event that interrupts the normal flow of a program (Dividing by zero,
         *             file not found, mismatch input type) Surround any dangerous code with a 
         *             try{} block, e.g. try{}, catch{}, finally{}
        */

        Scanner scanner = new Scanner(System.in);

        // Example 1 - The basics
        /*
        try{
            System.out.println(1 / 0);
        }
        catch(ArithmeticException e){
            System.out.println("YOU CAN DIVIDE BY ZERO!");
        }
        */

        // Example 2 - 

        try{
            System.out.print("Enter a number: ");
            int number = scanner.nextInt();
            System.out.println(number);
        }
        catch(InputMismatchException e){
            System.out.println("THAT WASN'T NUMBER");

        }
        catch(ArithmeticException e){
            System.out.println("YOU CAN DIVIDE BY ZERO!");
        }
        catch(Exception e){
            System.out.println("Something went wrong: " + e);
        }
        finally{
            scanner.close();
            System.out.println("This always Execute");
        }

        // scanner.close();

    }
}
