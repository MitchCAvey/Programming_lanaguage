import java.util.LinkedList;

public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * LinkedList = Stroes Nodes in 2 parts (Data + Address)
         *              Nodes are in Non-consecutive memor locations elements are linked using pointers
         *              
         *                                  Singly Linked List
         *                       Node                Node               Node
         *                  [data | address] -> [data | address] -> [data | address]
         * 
         *                                  Doubly Linked List
         *                       Node                                   Node
         *                  [address | data | address] <-> [address | data | address]
         * 
         * Advantages:
         * 1. Dynamic Data Structure (Allocates needed memory while running)
         * 2. Insertion and Deletion of Nodes is easy. O(1)
         * 3. No/Low memory waste
         * 
         * Disadvantages:
         * 1. Greater memory usage (additional pointer)
         * 2. No random access of elements (no index [i])
         * 3. Accessing/ Searching elements is more time consuming. O(n)
         * 
         * Uses:
         * 1. Implement Stacks/Queues
         * 2. GPS Navigation
         * 3. Music playlist
        */

        LinkedList<String> linkedList = new LinkedList<String>();

        // LinkedList as a Stack 
        // linkedList.push("A");
        // linkedList.push("B");
        // linkedList.push("C");
        // linkedList.push("D");
        // linkedList.push("F");

        // linkedList.pop(); // To remove the "head" item 

        // LinkedList as a Queue 
        linkedList.offer("A");
        linkedList.offer("B");
        linkedList.offer("C");
        linkedList.offer("D");
        linkedList.offer("F");

        // linkedList.poll(); // To remove the "head" item 

        linkedList.add(4, "E");
        // linkedList.remove("E");

        System.out.println(linkedList);

        System.out.println(linkedList.indexOf("F"));

        System.out.println(linkedList.peekFirst());
        System.out.println(linkedList.peekLast());
        
        linkedList.addFirst("0");
        linkedList.addLast("G");

        System.out.println(linkedList);

        
        String first = linkedList.removeFirst();
        String last = linkedList.removeLast();

        System.out.println("First: " + first);
        System.out.println("Last: " + last);
        System.out.println(linkedList);

    }
}
