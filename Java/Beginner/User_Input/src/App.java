import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        
        /*
        // The basics of getting input 
        Scanner scanner  = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = scanner.nextLine();

        System.out.print("Enter your age: ");
        int age = scanner.nextInt();

        System.out.print("What is your GPA? ");
        double gpa = scanner.nextDouble();

        System.out.print("Are you a student? (true/false):");
        boolean isStudent = scanner.nextBoolean();

        System.out.println("The name you entered is: " + name);
        System.out.println("You are " + age + " years old");
        System.out.println("Your GPA is: " + gpa);
        // System.out.println("Current student status: " + isStudent);

        if(isStudent){
            System.out.println("Your are enrolled as a student");
        }
        else{
            System.out.println("You are NOT enrolled");
        }

        scanner.close();
        */

        /*
        // Correct the new line character 

        System.out.print("Enter your age: ");
        int age2 = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Enter your favorite color: ");
        String color = scanner.nextLine();

        System.out.println("You are " + age2 + " years old");
        System.out.println("You like the " + color);

        scanner.close();

         */

        // Calculate area of a rectangle

        double width = 0;
        double height = 0;
        double area = 0;

        Scanner scanner  = new Scanner(System.in);
        
        System.out.print("Enter width: ");
        width = scanner.nextDouble();

        System.out.print("Enter height: ");
        height = scanner.nextDouble();

        area = width * height;

        System.out.println("The area is: " + area + "cm²");


        scanner.close();

    }
}
