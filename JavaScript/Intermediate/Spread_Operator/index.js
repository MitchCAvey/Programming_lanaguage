

/*
    Spread Operator = ... allows an iterable such as an array or string to be expanded into
                      seperate elements (unpacks the elements)
*/

let numbers = [1, 2, 3, 4, 5];
let maximum = Math.max(...numbers);
let minimum = Math.min(...numbers);
let username = "Mitch Avey";
let letters = [...username];
let joinedLetters = letters.join("-");
let fruits = ["apple", "orange", "banana"];
let newFruits = [...fruits];
let vegetables = ["carrots", "celery", "potatoes"];
let foods = [...fruits, ...vegetables, "eggs", "milk"];

console.log(numbers);
console.log(maximum);
console.log(minimum);
console.log(username);
console.log(letters);
console.log(joinedLetters);
console.log(fruits);
console.log(newFruits);
console.log(vegetables);
console.log(foods);























