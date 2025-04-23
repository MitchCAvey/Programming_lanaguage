// import java.util.ArrayList;

public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * Generics = A concept where you can write a class, interface, or method
         *            that is compatible with different data types.
         *            <T> type parameter (placeholder that gets replaced with a real type)
         *            <String> type argument (specifies the type)
        */

        /*
        // Example 1
        ArrayList<String> fruits = new ArrayList<>();

        fruits.add("apple");
        fruits.add("orange");
        fruits.add("banana");

        ArrayList<Integer> numbers = new ArrayList<>();

        numbers.add(1);
        numbers.add(2);
        numbers.add(3);

        ArrayList<Boolean> bools = new ArrayList<>();

        bools.add(true);
        bools.add(false);
        bools.add(true);
        */

        /*
        // Example 1.a - The basics
        Box<String> box1 = new Box<>();

        box1.setItem("banana");

        System.out.println(box1.getItem());

        Box<Integer> box2 = new Box<>();

        box2.setItem(5);

        System.out.println(box2.getItem());
        */

        Product<String, Double> product1 = new Product<>("Apple", 0.50);
        Product<String, Integer> product2 = new Product<>("Movie Ticket", 15);

        System.out.println(product1.getItem());
        System.out.println(product1.getPrice());

        System.out.println(product2.getItem());
        System.out.println(product2.getPrice());

    }
}
