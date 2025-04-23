

public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * overloaded methods = Methods that share the same name, but have different
         *                      parameters.
         *                      signature = name = parameters
        */

        // Example 1
        // System.out.println(add(1, 2));
        // System.out.println(add(1, 2, 3));
        // System.out.println(add(1, 2, 3, 4));

        // Example 2

        // String pizza = bakePizza("flat bread");
        // System.out.println(pizza);

        // String pizza = bakePizza("flat bread", "mozzarella");
        // System.out.println(pizza);

        String pizza = bakePizza("flat bread", "mozzarella", "pepperoni");
        System.out.println(pizza);


    }

    // Example 1
    /*
    static double add(double a, double b){
        return a + b;
    }

    static double add(double a, double b, double c){
        return a + b + c;
    }

    static double add(double a, double b, double c, double d){
        return a + b + c + d;
    }
    */

    // Example 2

    static String bakePizza(String bread){

        return bread + " Pizza";
    }

    static String bakePizza(String bread, String chesse){

        return chesse + " " + bread + " Pizza";
    }

    static String bakePizza(String bread, String chesse, String topping){

        return topping + " " + chesse + " " + bread + " Pizza";
    }

}
