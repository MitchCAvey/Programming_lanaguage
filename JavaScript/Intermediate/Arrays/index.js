

/*
    Array = A variable like structure that can hold more than 1 value
*/

let fruits = ["Apple", "Orange", "Banana"];

// console.log(fruit[0]);
// console.log(fruit[1]);
// console.log(fruit[2]);
console.log(`Prints all values in array: ${fruits}`);
console.log(`Prints value at index 0 in array: ${fruits[0]}`);
console.log(`Prints value at index 1 in array: ${fruits[1]}`);
console.log(`Prints value at index 2 in array: ${fruits[2]}`);

// Changing an exsiting value
fruits[0] = "Coconut";
console.log(`Value at index 0 in array was changed to: ${fruits[0]}`);

// Adding a new value in the next availabe index
fruits[3] = "Kiwi";
console.log(`Value at index 3 in array was changed to: ${fruits[3]}`);
console.log(`Prints all values in array after new value addition: ${fruits}`);

// This adds a new value to the array using the push() method
fruits.push("Blueberrys");
console.log(`Pushes a new value to the next available array index: ${fruits[4]}`);
console.log(`Prints all values in array after new value addition: ${fruits}`);

// This removes the last value of an array using the pop() method
fruits.pop();
console.log(`Pop has removed the value of Blueberry: ${fruits[4]} t`);
console.log(`Prints all values in array after new value addition: ${fruits}`);

// This adds a new value to the beginning of an array using the unshift() method
fruits.unshift("Mango");
console.log(`Unshift; Adding a new value to the start of the array: ${fruits[0]}`);
console.log(`Prints all values in array after new value addition: ${fruits}`);

// This removes a value from the beginning of an array using the shift() method
fruits.shift();
console.log(`shift; Removes a value to the start of the array: ${fruits[0]}`);
console.log(`Prints all values in array after new value addition: ${fruits}`);

// Working with an array's index length
fruits.unshift("Apple")
let numOfFruits = fruits.length;

console.log(`length number of fruit items in the fruits array: ${numOfFruits}`);

let index = fruits.indexOf("Apple");

console.log(`Using the indexOf method, the index of the 'Apple' value is: ${index}`)


console.log("Using a for loop to print out the values");

for(let i=0; i < fruits.length; i++){
    console.log(fruits[i]);
}

console.log("Reversing the order the values are printed");
for(let i = fruits.length - 1; i >= 0; i--){
    console.log(fruits[i]);
}

console.log("Print values with an 'Enhanced' for loop");
for(let fruit of fruits){
    console.log(fruit);
}

// Sorting the values in alpabetical order
console.log(fruits.sort());

// Reverse Sorting the values in alpabetical order
console.log(fruits.sort().reverse());



