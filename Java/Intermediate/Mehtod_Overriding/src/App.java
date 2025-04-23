


public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * Method overirding = When a subclass provies it's own implementation of a
         *                     method that is already defind. Allows for code reusability
         *                     and give specific impemenetations.
        */

        Dog dog = new Dog();
        Cat cat = new Cat();
        Fish fish = new Fish();

        dog.move();
        cat.move();
        fish.move();


    }
}
