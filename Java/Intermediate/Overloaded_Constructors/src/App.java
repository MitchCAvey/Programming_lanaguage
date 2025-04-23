

public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * overloaded constructors = Allow a class to have multiple constructors
         *                           with different parameter lists.
         *                           Enable objects to be initialized in various ways.
        */

        User user1 = new User("Melzanis");

        System.out.println("Username: " + user1.userName);
        System.out.println("Email: " + user1.email);
        System.out.println("Age: " + user1.age);

        User user2 = new User("Patrick", "PStar@aol.com");

        System.out.println("Username: " + user2.userName);
        System.out.println("Email: " + user2.email);
        System.out.println("Age: " + user2.age);

        User user3 = new User("Sandy", "SCheeks@gmail.com", 27);

        System.out.println("Username: " + user3.userName);
        System.out.println("Email: " + user3.email);
        System.out.println("Age: " + user3.age);

        User user4 = new User();

        System.out.println("Username: " + user4.userName);
        System.out.println("Email: " + user4.email);
        System.out.println("Age: " + user4.age);

    }
}
