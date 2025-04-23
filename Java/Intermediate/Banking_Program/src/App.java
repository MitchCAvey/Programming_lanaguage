import java.util.Scanner;

public class App {

    static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) throws Exception {
        
        // JAVA BANKING PROGRAM FOR BEGINNERS

       // DECLARE VARIABLES
    //    Scanner scanner = new Scanner(System.in);
       double balance = 0;
       boolean isRunning = true;
       int choice;

       
        while(isRunning){
            // DISPLAY MENU
            System.out.println("**************");
            System.out.println("BANING PROGRAM");
            System.out.println("**************");
            System.out.println("1. Show Balance");
            System.out.println("2. Deposit");
            System.out.println("3. Withdraw");
            System.out.println("4. Exit");
            System.out.println("**************");

            // GET AND PROCESS USERS CHOICE

            System.out.print("Enter your choice (1-4): ");
            choice = scanner.nextInt();

            // switch(choice){
            //     case 1 -> System.out.println("SHOW BALANCE");
            //     case 2 -> System.out.println("SHOW DEPOSIT");
            //     case 3 -> System.out.println("WITHDRAW");
            //     case 4 -> isRunning = false;
            //     default -> System.out.println("INVALID CHOICE");
            // }
            switch(choice){
                case 1 -> showBalance(balance);
                case 2 -> balance += deposit();
                case 3 -> balance -= withdraw(balance);
                case 4 -> isRunning = false;
                default -> System.out.println("INVALID CHOICE");
            }
        }

       // showBalance()

       // deposit()

       // withdraw()

       // EXIT MESSAGE
       System.out.println("***************************");
       System.out.println("Thank you! Have a nice day!");
       System.out.println("***************************");

       scanner.close();

    }

    static void showBalance(double balance){

        System.out.println("**************");
        System.out.printf("$%.2f\n", balance);
    }

    static double deposit(){

        double amount;

        System.out.print("Enter an amount: ");
        amount = scanner.nextDouble();

        if(amount < 0){
            System.out.println("Amount can't be negative");
            return 0;
        }
        else{
            return amount;
        }


        // scanner.close();
    }

    static double withdraw(double balance){

        double amount;

        System.out.print("Enter amount to be withdrawn: ");
        amount = scanner.nextDouble();

        if(amount > balance){
            System.out.println("INSUFFICIENT FOUNDS!!!!");
            return 0;
        }
        else if(amount < 0){
            System.out.println("Amount can't be negative!!");
            return 0;
        }
        else{
            return amount;
        }

        // return 0;
    }


}
