


public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * .toString() = Method inherited from the Object class. Used to return a string representation
         *               of an object. By default, it returns a hash code as a unique identifer. 
         *               It can be overridden to provide meaningful details. 
        */

        Car car = new Car("Ford", "Mustang", 2025, "Blue");
        Car car2 = new Car("Chevrolet", "Corvette", 2024, "Red");

        System.out.println(car);
        System.out.println(car2);

        // System.out.println(car.color + " " + car.year + " " + car.make + " " + car.model);



    }
}
