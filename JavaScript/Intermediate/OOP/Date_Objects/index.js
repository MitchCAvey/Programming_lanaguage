

/*
    Date objects = Objects that contain values that represent dates and times.
                   THese date objects can be changed and formatted

                   Date(year, month (0 - 11), day, hour, minute, second, ms)
*/

const date1 = new Date();

console.log(date1);

const year = date1.getFullYear();
const month = date1.getMonth();
const day = date1.getDate();
const time = date1.getTime();

console.log(month);

console.log(`The current date is ${year}/${month}/${day}\t current time is ${time}`);

const date2 = new Date(2024, 11, 31, 15, 30, 5);

console.log(date2);

const date3 = new Date("2024-01-02T12:00:00Z");

console.log(date3);

const date4 = new Date(1700000000000);

console.log(date4);

const date5 = new Date(0);

console.log(date5);

const date6 = new Date("2023-12-31");

const date7 = new Date("2024-01-01");

if(date7 > date6){
    console.log("HAPPY NEW YEAR!");
}














