

/*
    function declaration = define a reusable block of code that performs a specific task
*/

function hello(){
    console.log("Hello");
}

hello();

/*
    function expressions = a way to define functions as values or variables
*/


const hello2 = function(){
    console.log("Hello");
}

hello2();


// setTimeout(hello, 3000);

setTimeout(function(){
    console.log("Hello");
}, 3000);



//Example 2

const numbers = [1, 2, 3, 4, 5, 6];

function square(element){
    return Math.pow(element, 2);
}

function cube(element){
    return Math.pow(element, 3);
}

function evenNum(element){
    return element % 2 === 0;
}

function oddNum(element){
    return element % 2 !== 0;
}

function totalNum(accumulator, element){
    return accumulator + element;
}

const squares = numbers.map(square);
const cubes = numbers.map(cube);
const evennums = numbers.filter(evenNum);
const oddNums = numbers.filter(oddNum);
const total = numbers.reduce(totalNum);

console.log(`Not using function expressions (Squaring Numbers): ${squares}`);
console.log(`Not using function expressions (cubing Numbers): ${cubes}`);
console.log(`Not using function expressions (Even Numbers): ${evennums}`);
console.log(`Not using function expressions (Odd Numbers): ${oddNums}`);
console.log(`Not using function expressions (Reducing Numbers): ${total}`);

// The below will show case how to use function expressions
/*
    Function Expressions = A way to define functions as values or variables

        1. Callbacks in asynchronous operations
        2. Higer-Order Functions
        3. Closures
        4. Event Listerners
*/

const squares2 = numbers.map(function(element){
    return Math.pow(element, 2);
});

const cubes2 = numbers.map(function(element){
    return Math.pow(element, 3);
});

const evenNums2 = numbers.filter(function(element){
    return element % 2 === 0;
});

const oddNums2 = numbers.filter(function(element){
    return element % 2 !== 0;
});

const total2 = numbers.reduce(function(accumulator, element){
    return accumulator + element;
})

console.log(`using function expressions (Squaring Numbers): ${squares2}`);
console.log(`using function expressions (Squaring Numbers): ${cubes2}`);
console.log(`using function expressions (Even Numbers): ${evenNums2}`);
console.log(`Not using function expressions (Odd Numbers): ${oddNums2}`);
console.log(`Not using function expressions (Reducing Numbers): ${total2}`);
















