

/*
    functions = A section of reusable code.
                Declare code once, use it whenever you want.
                Call the function to execute that code.
*/

/*

//Basic structure of Functions in JavaScript
function happyBirthday(username, age){
    console.log("Happy birthday to you!");
    console.log("Happy birthday to you!");
    console.log(`Happy birthday dear ${username}!`);
    console.log("Happy birthday to you!");
    console.log(`You are ${age} years old!`);
}

happyBirthday("Mitch", 38);

*/

function addNums(x, y){
    // let result = x + y;
    // return result;
    return x + y;
}

function subtractNum(x, y){
    return x - y;
}

function multipyNum(x, y){
    return x * y;
}

function divideNum(x, y){
    return x / y;
}

function isEven(number){
    /*
    if(number % 2 === 0){
        return true;
    }
    else{
        return false;
    }
    */

    //The below is short hand using the ternary operator
    return number % 2 === 0 ? true : false;
}

function isValidEmail(emailAddr){

    /*
    if(emailAddr.includes("@")){
        return true;
    }
    else{
        return false;
    }
    */
   return emailAddr.includes("@") ? true : false;
}

let answer = addNums(8,4);
console.log(answer);

console.log(addNums(4,4));

console.log(subtractNum(8,3));

console.log(multipyNum(2,4));

console.log(divideNum(15,3));

console.log(isEven(10));

console.log(isValidEmail("mitchavey@acme.com"))





















