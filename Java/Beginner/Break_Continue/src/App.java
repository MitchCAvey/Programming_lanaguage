

public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * break = Break out of a loop (STOP!) 
         * continue = skip current iteration of a loop (SKIP)
        */

        for(int i = 0; i < 10; i++){

            // if(i == 5){
            //     break;
            // }

            if(i == 5){
                continue;
            }

            System.out.print(i + " ");
        }

    }
}
