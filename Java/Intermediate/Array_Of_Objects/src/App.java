public class App {
    public static void main(String[] args) throws Exception {
        

        // Car car1 = new Car("Mustang", "Red");
        // Car car2 = new Car("Corvette", "Blue");
        // Car car3 = new Car("Charger", "Yellow");

        // Car[] cars = new Car[3];
        // Car[] cars = {car1, car2, car3};

        // for(int i = 0; i < cars.length; i++){
        //     cars[i].drive();
        // }

        // for(Car car : cars){
        //     car.drive();
        // }

        // Creating annoymous objects
        Car[] cars = {new Car("Mustang", "Red"),
                      new Car("Corvette", "Blue"),
                      new Car("Charger", "Yellow")};

        for(Car car : cars){
            // car.drive();
            car.color = "Black";
        }

        for(Car car : cars){
            car.drive();
            // car.color = "Black"
        }

    }
}
