import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        
        Scanner scanner = new Scanner(System.in);
        // String[] foods = new String[4];
        String[] foods;
        int size;

        // foods[0] = "Pizza";
        // foods[1] = "Taco";
        // foods[2] = "Hamburger";

        // System.out.println(foods.length);

        System.out.print("What # of food do you want?: ");
        size = scanner.nextInt();
        scanner.nextLine();

        foods = new String[size];

        for(int i = 0; i < foods.length; i++){
            System.out.print("Enter a food: ");
            foods[i] = scanner.nextLine();
        }

        for(String food : foods){
            System.out.println(food);
        }
    
        scanner.close();

    }
}
