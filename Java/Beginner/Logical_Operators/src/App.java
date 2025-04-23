import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * && = AND - All conditions must be true
         * || = OR - Only one conditions needs to be true
         * !  = NOT 
         */

       // Example 1 
       /*  
       double temp = -10;
       boolean isSunny = true;
       
       if(temp <= 30 && temp >= 0 && isSunny){
        System.out.println("The weather is good!");
        System.out.println("It is SUNNY outside!");
       }
       else if(temp <= 30 && temp >= 0 && !isSunny){
        System.out.println("The weather is okay!");
        System.out.println("It is CLOUDY outside!");
       }
       else if(temp > 30 || temp < 0){
        System.out.println("The weather is bad!");
       }
       */
      
       // Example 2

       Scanner scanner = new Scanner(System.in);

       // username must be between 4 - 12 characters
       // username must not contain spaces or underscores 

       String username;

       System.out.print("Enter your username: ");
       username = scanner.nextLine();

       if(username.length() < 4 || username.length() > 12){
        System.out.println("Username must be between 4 - 12 characters!");
       }
       else if(username.contains(" ") || username.contains("_")){
        System.out.println("Username must not contain spaces or underscores!");
       }
       else{
        System.out.println("Welcome " + username);
       }

       scanner.close();

    }
}
