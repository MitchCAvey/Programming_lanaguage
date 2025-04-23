import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        
        // SHOPPING CART PROGRAM/ APP

        Scanner scanner = new Scanner(System.in);

        String item;
        double price;
        int quantity;
        char currency = '$';
        double total;

        System.out.print("What item would you like to buy?: ");
        item = scanner.nextLine();
        // System.out.println(item);

        System.out.print("What is the price for each?: ");
        price = scanner.nextDouble();
        // System.out.println(price);

        System.out.print("How many would you like?: ");
        quantity = scanner.nextInt();
        // System.out.println(quantity);

        total = price * quantity;
        System.out.println("\nYour have bought " + quantity + " " + item + "/s");
        System.out.println("Your total is: " + currency + total);


        scanner.close();

    }
}
