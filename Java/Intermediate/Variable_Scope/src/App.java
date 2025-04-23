

public class App {

    static int x = 3; // Class scope, which can be seen by everything
    public static void main(String[] args) throws Exception {
        
        // Variable Scope = Where a variable can be accessed or not

        // Example of local scope as this method was declared in the void main method
        int x = 1; 

        System.out.println(x);
        doSomething();

    }

    static void doSomething(){
        int x = 2; // x has local scope within doSomething() method

        System.out.println(x);
    }
}
