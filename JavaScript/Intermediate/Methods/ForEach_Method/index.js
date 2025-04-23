

/*
    forEach() = A method used to iterate over the elements of an array and apply a specified
                function (callback) to each element

            e.g. array.forEach(callback);
            element, index, array are provided
*/

let numbers = [1, 2, 3, 4, 5];

function display(element){
    console.log(element);
}

function double(element, index, array){
    array[index] = element * 2;
}

function triple(element, index, array){
    array[index] = element * 3;
}

function square(element, index, array){
    array[index] = Math.pow(element, 2);
}

function cube(element, index, array){
    array[index] = Math.pow(element, 3);
}

// numbers.forEach(double);
// numbers.forEach(triple)
// numbers.forEach(square);
numbers.forEach(cube);
numbers.forEach(display);

// Example 3

let fruits = ["apple", "orange", "banana", "coconut"];
let fruits2 = ["APPLE", "ORANGE", "BANANA", "COCONUT"];

function displayFruits(element){
    console.log(element);
}

function upperCase(element, index, array){
    array[index] = element.toUpperCase();
}

function lowerCase(element, index, array){
    array[index] = element.toLowerCase();
}

function capitalize(element, index, array){
    array[index] = element.charAt(0).toUpperCase() + element.slice(1);
}

// fruits.forEach(upperCase);
// fruits.forEach(display);

// fruits2.forEach(lowerCase);
// fruits2.forEach(display);

fruits.forEach(capitalize);
fruits.forEach(display);











