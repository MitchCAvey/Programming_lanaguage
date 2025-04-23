import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * While loop = Repeating some code forever or 
         *              while some condition remains true
         */

        Scanner scanner = new Scanner(System.in);

        // Example 1 - The Basics of While-Loops

        /* 
        String name = "";

        // if(name.isEmpty()){
        //     System.out.print("Enter your name: ");
        //     name = scanner.nextLine();
        // }

        while(name.isEmpty()){
            System.out.print("Enter your name: ");
            name = scanner.nextLine();
        }

        System.out.println("Hello " + name);
        */

        // Example 2 - Creating an infinite loop
        /* 
        while(1 == 1){
            System.out.println("HELP! I'M STUCK IN A LOOP");
        }
        */

        // Example 3
        /* 
        String response = "";

        while(!response.equals("Q")){
            System.out.println("You are playing a game");
            System.out.print("Press Q to quit: ");
            response = scanner.next().toUpperCase();
        }

        System.out.println("You have quit the game!");
        */

        // Example 4 - do while loop
        /* 
        int age = 0;

        System.out.print("Enter your age: ");
        age = scanner.nextInt();

        // while(age < 0){
        //     System.out.println("Your age can't be negative");
        //     System.out.print("Enter your age: ");
        //     age = scanner.nextInt();
        // }

        do{
            System.out.println("Your age can't be negative");
            System.out.print("Enter your age: ");
            age = scanner.nextInt();
        }while(age < 0);

        System.out.println("You are " + age + " years old!");
        */

        // Example 5 

        int number = 0;

        // while(number < 1 || number > 10){
        //     System.out.print("Enter a number between 1 - 10: ");
        //     number = scanner.nextInt();
        // }

        do{
            System.out.print("Enter a number between 1 - 10: ");
            number = scanner.nextInt();
        }while(number < 1 || number > 10);

        System.out.println("You picked " + number);
        
        scanner.close();

    }
}
