import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        
        // System.out.println(Math.PI);
        // System.out.println(Math.E);

        // double result;

        // result = Math.pow(2, 5);
        // result = Math.abs(-5);
        // result = Math.sqrt(9);
        // result = Math.round(3.14);
        // result = Math.ceil(3.14);
        // result = Math.floor(3.99);
        // result = Math.max(10, 20);
        // result = Math.min(10, 20);

        // System.out.println(result);

        /* 
        // HYPOTENUSE c = Math.sqrt(a² + b²)

        Scanner scanner = new Scanner(System.in);

        double a;
        double b;
        double c;

        System.out.print("Enter the length of side A: ");
        a = scanner.nextDouble();

        System.out.print("Enter the length of side B: ");
        b = scanner.nextDouble();

        c = Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2));

        System.out.println("The hypotenuse (side c) is: " + c + "cm");

        scanner.close();

        */

        /* Example - finding a radius
         * circumference = 2 * Math.PI * radius;
         * area = Math.PI * Math.pow(radius, 2);
         * volume = (4.0 / 3.0) * Math.PI * Math.pow(radius, 3);
         */

        Scanner scanner = new Scanner(System.in);

        double radius;
        double circumference;
        double area;
        double volume;

        System.out.print("Enter the radius: ");
        radius = scanner.nextDouble();

        circumference = 2 * Math.PI * radius;
        area = Math.PI * Math.pow(radius, 2);
        volume = (4.0 / 3.0) * Math.PI * Math.pow(radius, 3);

        // System.out.println("Circumference: " + circumference + "cm");
        // System.out.println("Area: " + area + "cm²");
        // System.out.println("Volume: " + volume + "cm³");

        System.out.printf("Circumference: %.2fcm\n", circumference);
        System.out.printf("Area: %.2fcm²\n", area);
        System.out.printf("Volume: %.2fcm³\n", volume);

        scanner.close();

    }
}
