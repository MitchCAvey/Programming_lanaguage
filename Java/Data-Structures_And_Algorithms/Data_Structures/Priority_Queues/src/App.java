import java.util.Collections;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * Priority Queue = A FIFO data structure that serves elements with
         *                  the highest priorities first before elements with lower
         *                  priority
        */

        /*
        // Example 1 - Standard Queue Setup
        Queue<Double> queue = new LinkedList<Double>();

        queue.offer(3.0);
        queue.offer(2.5);
        queue.offer(4.0);
        queue.offer(1.5);
        queue.offer(2.0);

        // Standard queue with no Priority (order)
        while(!queue.isEmpty()){
            System.out.println(queue.poll());
        }
        */

        /*
        // Example 1.a - Standard Ordering with Priority Queues
        Queue<Double> queue = new PriorityQueue<>();

        queue.offer(3.0);
        queue.offer(2.5);
        queue.offer(4.0);
        queue.offer(1.5);
        queue.offer(2.0);

        while(!queue.isEmpty()){
            System.out.println(queue.poll());
        }
        */

        /*
        //Example 1.b - Reverse Ordering
        Queue<Double> queue = new PriorityQueue<>(Collections.reverseOrder());

        queue.offer(3.0);
        queue.offer(2.5);
        queue.offer(4.0);
        queue.offer(1.5);
        queue.offer(2.0);

        while(!queue.isEmpty()){
            System.out.println(queue.poll());
        }
        */

        /*
        // Example 3 - Standard Ordering with Strings
        Queue<String> queue = new PriorityQueue<>();

        queue.offer("B");
        queue.offer("C");
        queue.offer("A");
        queue.offer("F");
        queue.offer("D");

        while(!queue.isEmpty()){
            System.out.println(queue.poll());
        }
        */

        // Example 3.a - Reversing the Order
        Queue<String> queue = new PriorityQueue<>(Collections.reverseOrder());

        queue.offer("B");
        queue.offer("C");
        queue.offer("A");
        queue.offer("F");
        queue.offer("D");

        while(!queue.isEmpty()){
            System.out.println(queue.poll());
        }

    }
}
