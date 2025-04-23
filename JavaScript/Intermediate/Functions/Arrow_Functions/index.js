

/*
    arrow functions = A concise way to write function expressions good for simple functions that you use 
                        only once (parameters) => some code
*/

// Example 1
function hello(){
    console.log("Hello");
}

hello();

const hello1 = function(){
    console.log("Hello a second time");
}

hello1();

const hello2 = () => console.log("Hello a third time");

hello2();

const hello3 = (name, age) => {console.log(`Hello ${name}, How are you today?`)
                            console.log(`Did you turn ${age} old today?`)};

hello3("Bob", 39);


// Example 2

function hello4(){
    console.log(`Hello a fourth time and 3 sec delay`);
}

setTimeout(hello4, 3000);

// From the above to the below
setTimeout(function(){
    console.log(`Hello a fith time and 4 sec delay and using function expressions`);
}, 4000);

setTimeout( () => console.log(`Hello a sixth time and 5 sec delay and using arrow functions`), 5000);

//Example 3

const numbers = [1, 2, 3, 4, 5, 6];


const squares = numbers.map((element) => Math.pow(element, 2));
const cubes = numbers.map((element) => Math.pow(element, 3));
const evenNums = numbers.filter((element) => element % 2 === 0);
const oddNums = numbers.filter((element) => element % 2 !== 0);
const total = numbers.reduce((accumulator, element) => accumulator + element);

console.log(`Arrow function result of squaring an array of numbers: ${squares}`);
console.log(`Arrow function result of cubing an array of numbers: ${cubes}`);
console.log(`Arrow function result finding the even numbers in an array: ${evenNums}`);
console.log(`Arrow function result finding the odd numbers in an array: ${oddNums}`);
console.log(`Arrow function result total of all numbers in an array: ${total}`);











