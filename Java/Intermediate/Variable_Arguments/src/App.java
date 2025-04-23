

public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * varargs = Allow a method to accept a varying # varying # of arguments
         *           makes methods more flexible, no need for overloaded methods
         *           java will pack the arguments into an array
         *           ... (ellipsis)
        */

        System.out.println(add(1,2,3,4,5,6));

        // System.out.println(average(3.45, 7.99, 8.55, 14.25, 4.68));
        System.out.println(average());

    }

    static int add(int... numbers){
        // System.out.println(numbers);
        int sum = 0;

        for(int number : numbers){
            sum += number;
        }

        return sum;
    }

    static double average(double... numbers1){

        double sum = 0;

        if(numbers1.length == 0){
            return 0.0;
        }

        for(double number : numbers1){
            sum += number;
        }

        return sum / numbers1.length;
    }
}
