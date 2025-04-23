

public class Student extends Person{

    double gpa;

    Student(String first, String last, double gpa){

        // this.first = first;
        // this.last = last;
        this.gpa = gpa;

        super(first, last);
    }

    void showGpa(){
        System.out.println(this.first + "'s gpa is: " + this.gpa);
    }

}
