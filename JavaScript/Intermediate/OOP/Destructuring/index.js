

/*
    destructuring = extract values from arrays and objects, then assign them to variables in a convenient way
    [] = to perform array destructuring
    {} = to perform object destructuring
*/

// Example 1: The basics - Swaping the value of two variables
/*
let a = 1;
let b = 2;

[a, b] = [b, a];

console.log(a);
console.log(b);
*/

// Example 2: Swaping 2 elements in an Array
/*
const colors = ["red", "green", "blue", "black", "white"];

console.log(colors);

[colors[0], colors[4]] = [colors[4], colors[0]];

console.log(colors);
*/

// Example 3: Assigning array elements to variables
/*
const colors2 = ["red", "green", "blue", "black", "white"];

const [firstColor, secondColor, thirdColor, ...extraColors] = colors2;

console.log(firstColor);
console.log(secondColor);
console.log(thirdColor);
console.log(extraColors);
*/

// Example 4: Extract values from objects
/*
const person1 = {
    firstName: "Spongebob",
    lastName: "SquarePants",
    age: 30,
    job: "Fry Cook",
}

const person2 = {
    firstName: "Patrick",
    lastName: "Star",
    age: 34,
}

// const {firstName, lastName, age, job} = person1;

// console.log(`Person 1`);
// console.log(`First Name: ${firstName}`);
// console.log(`Last Name: ${lastName}`);
// console.log(`Age: ${age}`);
// console.log(`Occupation: ${job}`);

const {firstName, lastName, age, job="Unemployed"} = person2;

console.log(`Person 1`);
console.log(`First Name: ${firstName}`);
console.log(`Last Name: ${lastName}`);
console.log(`Age: ${age}`);
console.log(`Occupation: ${job}`);
*/

// Example 5: Destructure in function parameters

const person1 = {
    firstName: "Spongebob",
    lastName: "SquarePants",
    age: 30,
    job: "Fry Cook",
}

const person2 = {
    firstName: "Patrick",
    lastName: "Star",
    age: 34,
}

function displayPerson({firstName, lastName, age, job="Unemployed"}){
    console.log(`Name: ${firstName} ${lastName}`);
    console.log(`Age: ${age}`);
    console.log(`Job: ${job}`);
}


displayPerson(person1);
displayPerson(person2)




