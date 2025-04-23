

public class App {
    public static void main(String[] args) throws Exception {
        
        // method = A block of reusable code that is executed when called ()

        // Example 1 
        /* 
        // System.out.println("Happy Birthday to you!");
        // System.out.println("Happy Birthday dear you!");
        // System.out.println("You are " + "x" + " years old!");
        // System.out.println("Happy Birthday to you!");

        // singHappyBirthday();
        // singHappyBirthday();

        String name = "Mitch";
        int age = 39;

        for(int i = 1; i <= 3; i++){
            singHappyBirthday(name, age);
        }
        */

        // Example 2
        System.out.println(square(9.25));

        double result = square(3.14);
        System.out.println(result);

        System.out.println(cube(3));

        String fullName = getFullName("Spongebob", "Squarepants");
        System.out.println(fullName);

        // Example 3
        int age = 39;

        if(ageCheck(age)){
            System.out.println("You may sign up!");
        }
        else{
            System.out.println("You must be 18+ to sign up!");
        }

    }

    // Example 1
    static void singHappyBirthday(String name, int age){
        System.out.println("Happy Birthday to you!");
        System.out.printf("Happy Birthday dear %s!\n", name);
        System.out.printf("You are %d years old!\n", age);
        System.out.println("Happy Birthday to you!\n");
    }

    // Example 2
    static double square(double number){

        return number * number;
    }

    // Example 2
    static double cube(double number){

        return number * number * number;
    }

    // Example 2
    static String getFullName(String first, String last){

        return first + " " + last;
    }

    // Example 3
    static boolean ageCheck(int age){
        
        if(age >= 18){
            return true;
        }
        else{
            return false;
        }
    }
}
