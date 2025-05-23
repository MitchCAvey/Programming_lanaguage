

public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * Aggregation = Represents a "has-a" relationship between objects.
         *               One object contains another object as part of its structure, 
         *               but the contained object(s) can exist independently.
        */

        Book book1 = new Book("The Fellowship of the Ring", 423);
        Book book2 = new Book("The Two Towers", 352);
        Book book3 = new Book("The Return of the King", 416);

        Book[] books = {book1, book2, book3};

        // System.out.println(book1.displayInfo());
        // System.out.println(book2.displayInfo());
        // System.out.println(book3.displayInfo());
        // System.out.println();

        // for(Book book : books){
        //     System.out.println(book.displayInfo());
        // }

        Library library = new Library("Toronto Public Library", 1884, books);

        library.displayInfo();

    }
}
