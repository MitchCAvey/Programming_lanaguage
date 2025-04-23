import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {

        // .substring() = A method used to extract a portion of a string
        //                .stubstring(start, end)

        // Example 1
        /* 
        String email = "melzanis@acme.com";

        String username = email.substring(0, email.indexOf("@"));

        String domain = email.substring(email.indexOf("@") + 1);

        System.out.println(username);
        System.out.println(domain);
        */

        // Example 2

        Scanner scanner = new Scanner(System.in);

        String email;
        String username;
        String domain;

        System.out.print("Enter your email: ");
        email = scanner.nextLine();
        // System.out.println(email);
        if(email.contains("@")){
            username = email.substring(0, email.indexOf("@"));
            domain = email.substring(email.indexOf("@") + 1);
    
            System.out.println("Username: " + username);
            System.out.println("Domain: " + domain);            
        }
        else{
            System.out.println("Emails must contain @!");
        }

        scanner.close();
    }
}
