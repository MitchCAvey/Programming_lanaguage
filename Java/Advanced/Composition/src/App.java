

public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * Composition = Represents a "part-of" relationship between objects.
         *               For example, an Engine is "part-of" a Car.
         *               Allows complex objects to be constructed from smaller objects
        */

        Car car = new Car("Corvette", 2025, "V8");

        System.out.println(car.model);
        System.out.println(car.year);
        System.out.println(car.engine.type);
        car.start();

    }
}
