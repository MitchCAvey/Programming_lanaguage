

public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * super = Refers to the parent class (subclass <- superclass)
         *         Used in consturctors and method overriding
         *         Calls the parent constructor to initialize attributes
        */


        Person person = new Person("Tom", "Riddle");
        Student student = new Student("Harry", "Potter", 3.25);
        Employee employee = new Employee("Rubeus", "Hagrid", 50000);

        person.showName();
        student.showName();
        System.out.println(student.gpa);
        student.showGpa();

        employee.showSalary();

    }
}
