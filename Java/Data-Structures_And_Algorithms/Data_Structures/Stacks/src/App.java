import java.util.Stack;

public class App {
    public static void main(String[] args) throws Exception {

        /*
         * stack = LIFO data structure. Last-In First-Out. Stores objects into a
         *         sort of "vertical tower"
         *         push() to add to the top
         *         pop() to remove from the top
        */

        Stack<String> stack = new Stack<String>();

        // System.out.println(stack.empty());
        stack.push("Minecraft");
        stack.push("Skyrim");
        stack.push("DOOM");
        stack.push("Borderlands");
        stack.push("FFVII");

        System.out.println(stack.empty());
        System.out.println(stack);

        // String myFavGame = stack.pop();

        // System.out.println(stack);
        // System.out.println(myFavGame);

        System.out.println(stack.peek());
        System.out.println(stack);

        System.out.println(stack.search("FFVII"));
        System.out.println(stack.search("DOOM"));
        System.out.println(stack.search("Minecraft"));

        /*
        // The below code will cause a Out Of Memory error message
        for(int i = 0; i < 100000000; i++){

            stack.push("Fallout76");
        }
        */

        /*
         * Uses of stacks?
         * 1. undo/redo features in text editors
         * 2. moving back/forward through browser history
         * 3. backtracking algorithms (maze, file directories)
         * 4. calling functions (call stack)
        */

    }
}
