import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        
        Scanner scanner = new Scanner(System.in);

        // int[] numbers = {1, 9, 2, 8, 3, 5, 4};
        String[] fruits = {"apple", "orange", "banana"};
        // String str_target = "pineapple";
        String str_target;
        // int target = 7;
        boolean isFound = false;

        // Conducting a linear search
        // for(int i = 0; i < numbers.length; i++){
        //     if(target == numbers[i]){
        //         System.out.println("Element found at index: " + i);
        //         isFound = true;
        //         break;
        //     }
        // }

        System.out.print("Enter a fruit to search: ");
        str_target = scanner.nextLine();

        for(int i = 0; i < fruits.length; i++){
            if(fruits[i].equals(str_target)){
                System.out.println("Element found at index: " + i);
                isFound = true;
                break;
            }
        }

        if(!isFound){
            System.out.println("Element not found in the array");
        }

        scanner.close();
    }
}
