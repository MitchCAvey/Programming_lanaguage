

public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * They help protect object data and add rules for accessing or modifying them.
         * GETTERS = Methods that make a field READABLE.
         * SETTERS = Methods that make a field WRITEABLE
        */

        Car car = new Car("Charger", "Yellow", 10000);

        // car.model = "Corvette";

        System.out.printf("%s - %s - %s", car.getModel(), car.getColor(), car.getPrice());

        // car.color = "Blue";
        // car.price = "5000";

        car.setColor("Blue");
        car.setPrice(15000);

        System.out.printf("\n%s - %s - %s", car.getModel(), car.getColor(), car.getPrice());
    }
}
