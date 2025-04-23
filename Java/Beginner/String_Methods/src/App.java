

public class App {
    public static void main(String[] args) throws Exception {

        String name = "Mitchell Avey";
        // String name = "      Mitchell Avey      ";
        // String name = "";
        // String name = "password";

        // int length = name.length();
        // char letter = name.charAt(0);
        // int index1 = name.indexOf("e");
        // int index2 = name.indexOf(" ");
        // int lastIndex = name.lastIndexOf("e");

        // name = name.toUpperCase();
        // name = name.toLowerCase();
        // System.out.println(name);
        // name = name.trim();
        // name = name.replace("e", "a");

        
        // System.out.println(length);
        // System.out.println(letter);
        // System.out.println(index1);
        // System.out.println(index2);
        // System.out.println(lastIndex);
        // System.out.println(name);
        // System.out.println(name.isEmpty());

        /* 
        if(name.isEmpty()){
            System.out.println("Your name is empty");
        }
        else{
            System.out.println("Hello " + name);
        }
        */

        /*
        if(name.contains(" ")){
            System.out.println("Your name contains a space");
        }
        else{
            System.out.println("Your name Doesn't contain any spaces");
        }
        */

        if(name.equalsIgnoreCase("password")){
            System.out.println("Your name can't be password");
        }
        else{
            System.out.println("Hello " + name);
        }
    }
}
