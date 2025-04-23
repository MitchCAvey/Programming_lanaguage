

public class App {
    public static void main(String[] args) throws Exception {
        
        // printf() = Is a method used to format ouput

        // %[flags][width][.precision][specifier-character]

        // Exmaple 1 - Basics
        /* 
        String name = "Spongebob";
        char firstLetter ='S';
        int age = 30;
        double height = 60.5;
        boolean isEmployed = true;

        System.out.printf("Hello %s\n", name);
        System.out.printf("Your name starts with a %c\n", firstLetter);
        System.out.printf("Your age is: %d\n", age);
        System.out.printf("Height is %.2fcm\n", height);
        System.out.printf("Employment Status: %b\n", isEmployed);

        System.out.printf("%s is %d years old", name, age);

        */

        // Example 2 - Working with the [.precision]
        /* 
        double price1 = 9.99;
        double price2 = 100.15;
        double price3 = -54.01;

        // System.out.printf("%.1f\n", price1);
        // System.out.printf("%.1f\n", price2);
        // System.out.printf("%.1f\n", price3);

        
        //  Flags -
        //  + = output a plus
        //  , = comma grouping separator
        //  ( = negative numbers are enclosed in ()
        //  space = display a minus if negative, space if positive
         

        double price4 = 9000.99;
        double price5 = 100000.15;
        double price6 = -54000.01;

        // Using the '+' flag
        // System.out.printf("%+.2f\n", price4);
        // System.out.printf("%+.2f\n", price5);
        // System.out.printf("%(.2f\n", price6);

        // Using the ',' flag
        // System.out.printf("%,.2f\n", price4);
        // System.out.printf("%,.2f\n", price5);
        // System.out.printf("%,.2f\n", price6);

        // Using the '(' flag
        // System.out.printf("%(,.2f\n", price4);
        // System.out.printf("%(,.2f\n", price5);
        // System.out.printf("%(,.2f\n", price6);

        // Using the 'space'/" " flag
        System.out.printf("% ,.2f\n", price4);
        System.out.printf("% ,.2f\n", price5);
        System.out.printf("% ,.2f\n", price6);

        */

        //Example - Working with the [width]

        // [width]

        // 0 = zero padding
        // number = right justified padding
        // negative number = left justified

        int id1 = 1;
        int id2 = 23;
        int id3 = 456;
        int id4 = 7890;

        // System.out.printf("%04d\n", id1);
        // System.out.printf("%04d\n", id2);
        // System.out.printf("%04d\n", id3);
        // System.out.printf("%04d\n", id4);

        // System.out.printf("%4d\n", id1);
        // System.out.printf("%4d\n", id2);
        // System.out.printf("%4d\n", id3);
        // System.out.printf("%4d\n", id4);

        System.out.printf("%-4d\n", id1);
        System.out.printf("%-4d\n", id2);
        System.out.printf("%-4d\n", id3);
        System.out.printf("%-4d\n", id4);

    }
}
