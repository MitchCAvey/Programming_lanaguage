import java.util.Random;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * Object = An entity that holds data (attributes) and can perfrom actions
         *          (methods). It is a reference data type
        */

        // Scanner scanner = new Scanner(System.in);
        // Random random = new Random();

        Car car = new Car();
        Car car2 = new Car();

        // car.isRunning = true;

        // System.out.println(car);
        // System.out.println(car.model);
        // System.out.println(car.make);
        // System.out.println(car.year);
        // System.out.println(car.price);
        // System.out.println(car.isRunning);

        System.out.println(car.isRunning);
        car.start();
        System.out.println(car.isRunning);
        car.stop();
        System.out.println(car.isRunning);
        car.drive();
        car.breaks();


        // scanner.close();

    }
}
