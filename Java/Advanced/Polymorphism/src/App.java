

public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * Polymorphism = "POLY" = "MANY"
         *                "MORPH" = "SHAPE"
         * 
         *                Objects can identify as other objects.
         *                Objects can be treated as objects of a common superclass. 
        */

        Car car = new Car();
        Bike bike = new Bike();
        Boat boat = new Boat();

        // car.go();
        // bike.go();
        // boat.go();

        // Car[] cars = {car, bike, boat};
        Vehicle[] vehicles = {car, bike, boat};

        for(Vehicle vehicle : vehicles){
            vehicle.go();
        }

    }
}
