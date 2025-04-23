

/*
    sort() = A method used to sort elements of an array in place. It sorts elements as
             strings in lexicopraphic order, not alphabetical
             Lexicopgraphic = (alphabet + numbers + symbols) as strings            
*/

let fruits = ["apple", "orange", "banana", "coconut", "pineapple"];
let numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1];

fruits.sort();

console.log(fruits);

numbers.sort((a, b) => a - b);

console.log(numbers);

// For reverse order
numbers.sort((a, b) => b - a);

console.log(numbers);

const people = [
    {name: "Spongebob", age: 30, gpa: 3.0},
    {name: "Patrick", age: 37, gpa: 1.5},
    {name: "Squidward", age: 51, gpa: 2.5},
    {name: "Sandy", age: 27, gpa: 4.0}
];

people.sort((a, b) => a.age - b.age);

console.log(people);

people.sort((a, b) => b.age - a.age);

console.log(people);

people.sort((a, b) => b.name.localeCompare(a.name));

console.log(people);

people.sort((a, b) => a.name.localeCompare(b.name));

console.log(people);