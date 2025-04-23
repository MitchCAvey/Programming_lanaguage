import java.util.Scanner;

public class App {
    public static void main(String[] args) throws InterruptedException {

        // for loop = execute some code a CERTAIN amount of times

        // for(int i = 0; i < 10; i++){
        //     System.out.println(i + "." + " Pizza");
        // }

        // for(int i = 1; i <= 10; i++){
        //     System.out.println(i + "." + " Pizza");
        // }

        // for(int i = 10; i > 0; i--){
        //     System.out.println(i + "." + " Pizza");
        // }

        // for(int i = 1; i <= 10; i+=3){
        //     System.out.println(i + "." + " Pizza");
        // }

        // for(int i = 10; i > 0; i-=2){
        //     System.out.println(i + "." + " Pizza");
        // }

        // Scanner scanner = new Scanner(System.in);

        // System.out.print("Enter # of times to loop: ");
        // int max = scanner.nextInt();

        // for(int i = 0; i < max; i++){
        //     System.out.println(i);
        // }

        // scanner.close();

        Scanner scanner = new Scanner(System.in);

        // int start = 10;

        System.out.print("How many seconds to countdown from?: ");
        int start = scanner.nextInt();

        for(int i = start; i > 0; i--){
            System.out.println(i);
            Thread.sleep(1000);
        }

        System.out.println("Happy New Years!!!");

        scanner.close();

    }
}
