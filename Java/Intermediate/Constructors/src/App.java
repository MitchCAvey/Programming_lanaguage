

public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * constructor = A special method to initialize objects you can pass 
         *               arguments to a constructor and set up inital values
        */

        Student student1 = new Student("Spongebob", 30, 3.2);
        Student student2 = new Student("Sandy", 27, 4.2);
        Student student3 = new Student("Patrick", 32, 2.5);
        Student student4 = new Student("Squidward", 45, 3.1);

        // System.out.println("Student 1 Name: " + student1.name);
        // System.out.println("Student 1 Age: " + student1.age);
        // System.out.println("Student 1 GPA: " + student1.gpa);
        // System.out.println("Student 1 Is Enrolled: " + student1.isEnrolled);
        // System.out.println();
        // System.out.println("Student 2 Name: " + student2.name);
        // System.out.println("Student 2 Age: " + student2.age);
        // System.out.println("Student 2 GPA: " + student2.gpa);
        // System.out.println("Student 2 Is Enrolled: " + student2.isEnrolled);
        // System.out.println();
        // System.out.println("Student 3 Name: " + student3.name);
        // System.out.println("Student 3 Age: " + student3.age);
        // System.out.println("Student 3 GPA: " + student3.gpa);
        // System.out.println("Student 3 Is Enrolled: " + student3.isEnrolled);
        // System.out.println();
        // System.out.println("Student 4 Name: " + student4.name);
        // System.out.println("Student 4 Age: " + student4.age);
        // System.out.println("Student 4 GPA: " + student4.gpa);
        // System.out.println("Student 4 Is Enrolled: " + student4.isEnrolled);

        student1.study();
        student2.study();
        student3.study();
        student4.study();


    }
}
