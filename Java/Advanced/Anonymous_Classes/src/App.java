

public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * Anonymous class = A class that doesn't have a name. Cannot be reused.
         *                   Add custom behavior without having to create a new class. 
         *                   Often used for one time uses (TimerTask, Runnable, callbacks) 
        */

        Dog dog1 = new Dog();

        dog1.speak();

        // TalkingDog talkingDog = new TalkingDog1();

        // talkingDog.speak();


        // Creating an Anonymous class
        Dog dog2 = new Dog(){

            @Override
            void speak(){
                System.out.println("Scooby Doo says *Ruh Roh");
            }
        };

        dog2.speak();


    }
}
