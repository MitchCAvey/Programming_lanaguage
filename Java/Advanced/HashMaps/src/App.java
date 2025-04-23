import java.util.HashMap;

public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * HashMap = A data structure that stores key-value pairs. 
         *           Keys are unique, but Values can be duplicated
         *           Does not maintain any order, but is memory efficient
         *           HashMap<Key, Values>
        */

        HashMap<String, Double> map = new HashMap<>();

        // Putting values in a HashMap
        map.put("Apple", 0.50);
        map.put("Orange", 0.75);
        map.put("Banana", 0.25);
        // map.put("Orange", 100000.00);// overwrites the value of a duplicate key
        map.put("Coconut", 1.00);

        // System.out.println(map);

        // map.remove("Apple");

        // System.out.println(map);

        // System.out.println(map.get("Coconut"));

        // System.out.println(map.containsKey("Apple"));
        // System.out.println(map.containsKey("Pineapple"));

        // if(map.containsKey("Pineapple")){
        //     System.out.println(map.get("Apple"));
        // }
        // else{
        //     System.out.println("Key Not Found!");
        // }

        // System.out.println(map.containsValue(1.00));

        // System.out.println(map.size());

        for(String key : map.keySet()){
            // System.out.println(key + " : $" + map.get(key));
            System.out.printf("%s : $%.2f\n",key, map.get(key));
        }


    }
}
