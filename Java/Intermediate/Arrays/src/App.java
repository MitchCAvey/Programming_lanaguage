import java.util.Arrays;

public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * array = A collection of values of the same data type
         *         * Think of it as a variable that can store more than 1
         *           value *
        */

        String fruit = "Apple";
        String[] fruits = {"Apple", "Banana", "Orange", "Coconut"};
        int numOfFruits = fruits.length;
        

        System.out.println(fruit);

        System.out.println(fruits); // returns a memory location
        System.out.println(fruits[0]); // prints the first element in the array
        System.out.println(fruits[1]);
        System.out.println(fruits[2]);
        System.out.println(fruits[3]);


        // Re-assigning a value at a specific index location
        fruits[0] = "Pineapple";
        System.out.println("\n" + fruits[0]);
        System.out.println(fruits[1]);
        System.out.println(fruits[2]);
        System.out.println(fruits[3]);

        System.out.println("# of elements/index in the array: " + numOfFruits);

        for(int i = 0; i < fruits.length; i++){
            System.out.println(fruits[i]);
        }

        // This is a for-each loop
        for(String fruit1 : fruits){
            System.out.println(fruit1);
        }

        Arrays.sort(fruits);

        System.out.println("\nArray After being sorted: ");
        for(String fruit2 : fruits){
            System.out.println(fruit2);
        }

        Arrays.fill(fruits, "Pineapple");
        for(String fruit2 : fruits){
            System.out.println(fruit2);
        }


    }
}
