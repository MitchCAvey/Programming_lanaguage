import java.time.Instant;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

public class App {
    public static void main(String[] args) throws Exception {
        
        /*
         * How to work with DATES & TIMES using Java
         * (LocalDate, LocalTime, LocalDateTime, UTC timestamp)
        */

        LocalDate date = LocalDate.now();

        System.out.println(date);

        LocalTime time = LocalTime.now();

        System.out.println(time);

        LocalDateTime dateTime = LocalDateTime.now();

        System.out.println(dateTime);

        Instant instant = Instant.now();

        System.out.println(instant);

        // Custom format
        LocalDateTime dateTime2 = LocalDateTime.now();

        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MM-dd-yyyy HH:mm:ss");

        String newDateTime = dateTime2.format(formatter);

        System.out.println(newDateTime);

        LocalDate date1 = LocalDate.of(2024, 12, 25);

        System.out.println(date1);

        // LocalDateTime dateTime3 = LocalDateTime.of(2024, 12, 25, 12,0, 0);
        // LocalDateTime dateTime4 = LocalDateTime.of(2025, 1, 1, 0,0, 0);
        // LocalDateTime dateTime3 = LocalDateTime.of(2025, 1, 2, 12,0, 0);
        // LocalDateTime dateTime4 = LocalDateTime.of(2025, 1, 1, 0,0, 0);
        LocalDateTime dateTime3 = LocalDateTime.of(2025, 1, 1, 0,0, 0);
        LocalDateTime dateTime4 = LocalDateTime.of(2025, 1, 1, 0,0, 0);

        System.out.println(dateTime3);
        System.out.println(dateTime4);

        if(dateTime3.isBefore(dateTime4)){
            System.out.println(dateTime3 + " is earlier than " + dateTime4);
        }
        else if(dateTime3.isAfter(dateTime4)){
            System.out.println(dateTime3 + " is later than " + dateTime4);
        }
        else if(dateTime3.isEqual(dateTime4)){
            System.out.println(dateTime3 + " is equal to " + dateTime4);
        }

    }
}
