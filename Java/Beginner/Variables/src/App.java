public class App {
    public static void main(String[] args) throws Exception {
        /* ❎variable = a reusable container for a value
         *            a variable behaves as if it was the value it contains
         * 
         * 🟥 Primitive = simple value stored directly in memory (stack)
         * 🟦 Reference = memory address (stack) that points to the (heap)
         * 
         * 🟥 Primitive vs 🟦 Reference
         *    ----------       ---------
         *    int               string
         *    double            array
         *    char              object
         *    boolean
         * 
         * 2 Steps to creating a variable
         * ------------------------------
         * 1. declaration 
         * 2. assignment
         *   
         */

        System.out.println("\nWorking with integers & doubles - ");
        int age;
        // System.out.println(age);
        age = 38;
        System.out.println("Your age is: " + age);

        int year = 2025;
        System.out.println("The year is: " + year);

        int quantity = 1;
        System.out.println("The quantity is: " + quantity);

        double price = 19.99;
        System.out.println("Purchase Price is $" + price);

        double gpa = 3.5;
        System.out.println("Your current GPA is:" + gpa);

        double temperature = -12.5;
        System.out.println("The current Temp is:" + temperature);

        System.out.println("\nWorking with char's - ");

        char grade = 'A';
        System.out.println("Your Math test grade is: " + grade);
        
        char symbol = '!';
        System.out.println("A random symbol: " + symbol);
        
        char currency = '$';
        System.out.println("Purchase price: " + currency + price);

        System.out.println("\nWorking with booleans - ");

        boolean isStudent = true;
        // System.out.println("Is Student: " + isStudent);

        boolean forSale = false;
        // System.out.println("On Sale status: " + forSale);

        boolean isOnline = true;
        // System.out.println("Online Status" + isOnline);

        if(isStudent){
            System.out.println("Is Student: " + isStudent);
        }

        if(!forSale){
            System.out.println("On Sale status: " + forSale);
        }

        if(isOnline){
            System.out.println("Online Status: " + isOnline);
        }

        System.out.println("\nWorking with Strings - ");

        String name = "Melzanis";
        System.out.println("Your Name is: " + name);

        String food = "Pizza";
        System.out.println("Your favorite food is: " + food);

        String email = "fake@acme.com";
        System.out.println("Your email is: " + email);

        String car = "Mustang";
        System.out.println("Your favorite car is: " + car);

        String color = "Blue";
        System.out.println("Your favorite color is: " + color);

        System.out.println("Your choice is a " + color + " " + year + " " + car);

        double price2 = 19999.99;
        System.out.println("The price is: " + currency + price2);

        if(forSale){
            System.out.println("There is a " + car + "for sale");
        }
        else{
            System.out.println("The " + car + " not for sale!");
        }

    }
}
