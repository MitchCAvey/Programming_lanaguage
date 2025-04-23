

public class Student {

    String name;
    int age;
    double gpa;
    boolean isEnrolled;

    Student(String name, int age, double gpa){
        this.name = name;
        this.age = age;
        this.gpa = gpa;
        this.isEnrolled = true;

    }

    // Student(String a, int b, double c){
    //     this.name = a;
    //     this.age = b;
    //     this.gpa = c;

    // }

    void study(){
        System.out.println(this.name + " is studying");
    }

}
