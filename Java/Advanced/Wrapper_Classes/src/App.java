

public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * Wrapper classes = Allow primitive values (int, char, double, boolean)
         *                   to be used as objects. "Wrap them in an object"
         *                   Generally, don't wrap primitives unless you need an object. 
         *                   Allows use of Collections framework and static Utility Methods
        */

        // int a = 123;

        // Deprecated
        // Integer a = new Integer(123);
        // Double b = new Double(3.14);
        // Character c = new Character('$');
        // Boolean d = new Boolean(true);

        // Autoboxing
        /*
        Integer a = 123;
        Double b = 3.14;
        Character c = '$';
        Boolean d = true;
        String e = "Pizza";
        */

        // Unboxing
        /*
        int xa = a;
        double xb = b;
        char xc = c;
        boolean xd = d;

        String xe = Integer.toString(123);
        String xf = Double.toString(3.14);
        String xg = Character.toString('@');
        String xh = Boolean.toString(false);

        String xi = xe + xf + xg + xh;

        System.out.println(xi);
        */

        // Parsing
        /*
        int a = Integer.parseInt("123");
        double b = Double.parseDouble("3.14");
        char c = "Pizza".charAt(0);
        boolean d = Boolean.parseBoolean("true");

        String x = a + b + c + d;

        */

        char letter = 'm';

        System.out.println(Character.isLetter(letter));
        System.out.println(Character.isUpperCase(letter));



    }
}
