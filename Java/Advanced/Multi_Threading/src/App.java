

public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * Multithreading = Enables a program to run multiple threads concurrently
         *                  (Thread = A set of instructions that run independently)
         *                  Useful for background tasks or time-consuming operations
        */

        // MyRunnable myRunnable = new MyRunnable();
        
        // Thread thread = new Thread(myRunnable);
        Thread thread1 = new Thread(new MyRunnable("Ping"));
        Thread thread2 = new Thread(new MyRunnable("Pong"));

        System.out.println("GAME START!");

        thread1.start();
        thread2.start();

        try{
            thread1.join();
            thread2.join();
        }
        catch(InterruptedException e){
            // throw new RuntimeException(e);
            System.out.println("Main thread was interrupted!");
        }

        System.out.println("GAME OVER!");

    }
}
