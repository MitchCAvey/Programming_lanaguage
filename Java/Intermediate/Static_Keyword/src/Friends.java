

public class Friends {

    String name;
    static int numOfFriends;

    Friends(String name){
        this.name = name;
        numOfFriends++;
    }

    static void showFriends(){
        System.out.println("You have " + numOfFriends + " Total Friends");
    }
}
