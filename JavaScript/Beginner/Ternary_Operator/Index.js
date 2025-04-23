

/*
    ternary operator = A shortcut to if(){} and else{} statements that helps to 
                       assign a variable based on a condition.
        
        e.g. condition ? codeIfTrue : codeIfFalse;
*/
/*
let age = 38;

let message;

if(age >= 18){
    message = "You're an adult";
}
else{
    message = "You're a minor";
}

console.log(message)

*/

// BASIC EXAMPLE: The below is short hand for the above
/*
let age1 = 17;

let message1 = age1 >= 18 ? "You're an adult" : "You're a minor";

console.log(message1)

*/

/*
// Example 1.
let time = 9;
let greeting = time < 12 ? "Good morning" : "Good afternoon";

console.log(greeting)

*/

/*
// Example 2.
let isStudent = true;

let message = isStudent ? "You are a student" : "You are NOT a student";

console.log(message);

*/


let purchaseAmount = 125;
let discount = purchaseAmount >= 100 ? 10 : 0;

console.log(`Your total is $${purchaseAmount -purchaseAmount * (discount / 100)}`)




