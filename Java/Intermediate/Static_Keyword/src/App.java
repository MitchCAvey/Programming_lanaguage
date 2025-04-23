


public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * static = Makes a variable or method belong to the class rather than to any specific object. 
         *          Commonly used for utility methods or shared resources.
        */

        Friends friends1 = new Friends("Bob");
        Friends friends2 = new Friends("Jack");
        Friends friends3 = new Friends("Melzanis");
        Friends friends4 = new Friends("Amicia");
        Friends friends5 = new Friends("John");

        // System.out.println(friends1);
        // System.out.println(friends1.numOfFriends);
        // System.out.println(friends2);
        // System.out.println(friends2.numOfFriends);
        // System.out.println(friends3);
        // System.out.println(friends3.numOfFriends);

        System.out.println(Friends.numOfFriends);
        Friends.showFriends();

        // Math.round(3.99);


    }
}
