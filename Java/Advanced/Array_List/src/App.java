import java.util.ArrayList;
// import java.util.Collections;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * ArrayList = A resizeable array that stores objects (autoboxing).
         *             Arrays are fixed in size, but ArrayLists can change.
        */

        // Creating an Integer ArrayList
        // ArrayList<Integer> list1 = new ArrayList<>();

        // list1.add(3);
        // list1.add(1);
        // list1.add(2);

        // System.out.println(list1);

        // Creating an Double ArrayList
        // ArrayList<Double> list2 = new ArrayList<>();

        // list2.add(3.14);
        // list2.add(1.25);
        // list2.add(2.98);

        // System.out.println(list2);

        // Creating an String ArrayList
        // ArrayList<String> list3 = new ArrayList<>();

        // list3.add("Apple");
        // list3.add("Banana");
        // list3.add("Orange");
        // list3.add("Coconut");

        // System.out.println(list3);

        // list3.remove(1);

        // System.out.println(list3);

        // Replacing the value with a new value 
        // list3.set(1, "Pineapple");

        // System.out.println(list3);

        // System.out.println(list3.get(2));

        // System.out.println(list3.size());

        // Collections.sort(list3);

        // System.out.println(list3);

        // for(String item : list3){
        //     System.out.println(item);
        // }

        Scanner scanner = new Scanner(System.in);

        ArrayList<String> foods = new ArrayList<>();

        System.out.print("Enter # of food you like: ");
        int numOfFood = scanner.nextInt();
        scanner.nextLine();

        for(int i = 1; i <= numOfFood; i++){
            System.out.print("Enter food #" + i + ": ");
            String food = scanner.nextLine();
            foods.add(food);
        }

        System.out.println(foods);

        scanner.close();

    }
}
