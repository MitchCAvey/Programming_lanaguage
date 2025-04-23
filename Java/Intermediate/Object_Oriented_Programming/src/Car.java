

public class Car {

    // This are attributes that a class has
    String make = "Ford";
    String model = "Mustang";
    int year = 2025;
    double price = 58000.99;
    boolean isRunning = false;

    void start(){
        System.out.println("You start the engine");
        isRunning = true;
    }

    void stop(){
        System.out.println("You stop the engine");
        isRunning = false;
    }

    void drive(){
        System.out.println("You drive the " + model);
    }

    void breaks(){
        System.out.println("You break the " + model);
    }


}
