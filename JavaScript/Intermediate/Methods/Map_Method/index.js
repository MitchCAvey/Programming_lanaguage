

/*
    .map() = accepts a callback and applies that function to each element of an array,
             then returns a new array
*/

const numbers = [1, 2, 3, 4, 5];
// const square = numbers.map(square);

function square(element){
    return Math.pow(element, 2);
}

function cube(element){
    return Math.pow(element, 3);
}

const squares= numbers.map(square);

console.log(squares)

const cubed = numbers.map(cube);

console.log(cubed);

//Example 2

const students = ["Spongebob", "Patrick", "Squidward", "Sandy"];

function upperCase(element){
    return element.toUpperCase();
}

function lowerCase(element){
    return element.toLowerCase();
}

const studentsUpper = students.map(upperCase);

console.log(studentsUpper);

const studentsLower = students.map(lowerCase);

console.log(studentsLower);


// Example 3

const dates = ["2023-09-07", "1986-05-09", "1986-01-26"];

function formatDates(element){
    const parts = element.split("-");
    return `${parts[1]}/${parts[2]}/${parts[0]}`;
}

const formatedDates = dates.map(formatDates);

console.log(formatedDates);





















