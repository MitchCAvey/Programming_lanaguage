

public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * 2D array = An array where each element is an array
         *            Useful for stroing a matrix of data
        */

        // Example 1 - The basics
        /*
        String[] fruits = {"apple", "orange", "banana"};
        String[] vegetables = {"potato", "onion", "carrot"};
        String[] meats = {"chicken", "pork", "beef", "fish"};

        String[][] groceries = {fruits, vegetables, meats};
        // String[][] groceries = {{"apple", "orange", "banana"},
        //                         {"potato", "onion", "carrot"},
        //                         {"chicken", "pork", "beef", "fish"}};

        // accessing a 2D array's elements
        groceries[0][0] = "pineapple";
        groceries[1][0] = "celery";
        groceries[2][3] = "salom";

        for(String[] foods : groceries){
            for(String food : foods){
                System.out.print(food + " ");
            }
            System.out.println();
        }
        */

        // Example 2 
        char[][] telepone = {{'1', '2', '3'},
                             {'4', '5', '6'},
                             {'7', '8', '9'},
                             {'*', '0', '#'}};

        for(char[] row : telepone){
            for(char number : row){
                System.out.print(number + " ");
            }
            System.out.println();
        }

    }
}
