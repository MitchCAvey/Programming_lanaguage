import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        
        // nested loop = A loop inside another loop
        //               Used often with matrix/matrices or DS & A (Data Structures & Algorithms)

        // for(int i = 1; i <= 9; i++){
        //     System.out.print(i + " ");
        // }

        // for(int i = 1; i <= 3; i++){
        //     for(int j = 1; j <= 9; j++){
        //         System.out.print(j + " ");
        //     }
        //     System.out.println();
        // }

        Scanner scanner = new Scanner(System.in);

        int rows;
        int columns;
        char symbol;

        
        System.out.print("Enter the # of rows: ");
        rows = scanner.nextInt();

        System.out.print("Enter the # of columns: ");
        columns = scanner.nextInt();

        System.out.print("Enter the symbol to use: ");
        symbol = scanner.next().charAt(0);

        for(int i = 0; i < rows; i++){
            for(int j = 0; j < columns; j++){
                System.out.print(symbol + " ");
            }
            System.out.println();
        }


        scanner.close();
    }
}
