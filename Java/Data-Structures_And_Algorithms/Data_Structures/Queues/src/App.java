import java.util.Queue;
import java.util.LinkedList;

public class App {
    public static void main(String[] args) throws Exception {

        /*
         * Queue = FIFO data structure. First-In First-Out (ex. A line of people). A collection designed for 
         *         holding elements prior to processing Linear data structure
         * 
         *         add      = enqueue, offer()
         *         remove   = dequeue, poll()
         * 
         * Where are queues useful?
         * 
         * 1. Keyboard Buffer (letters should apear on the screen in the order theu're pressed)
         * 2. Printer Queue (Print jobs should be completed in order)
         * 3. Used in LinkedLists, PriorityQueues, Breadth-first search
        */

        Queue<String> queue = new LinkedList<String>();

        // System.out.println(queue.isEmpty());

        queue.offer("Karen");
        queue.offer("Chad");
        queue.offer("Steve");
        queue.offer("Harold");

        // System.out.println(queue.isEmpty());

        // System.out.println(queue);
        // // System.out.println(queue.peek());
        // queue.poll();
        // System.out.println(queue);
        // queue.poll();
        // System.out.println(queue);

        // System.out.println(queue.size());

        // System.out.println(queue.contains("Harold"));
        

    }
}
