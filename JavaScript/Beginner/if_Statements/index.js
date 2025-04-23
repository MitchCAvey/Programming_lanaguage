

/*
    IF STATEMENTS = if a condition is true, execute some code 
                    if not, do something else

*/


// Example 1. basic if-else Statement
/*
let age = 25;

if(age >= 35){
    console.log("You are old enough to enter this site");
}
else{
    console.log("You must be 18+ to enter this site");
}

*/

// Example 2. 
/*
let time = 16;

if(time < 12){
    console.log("Good Morning")
}
else{
    console.log("Good Afternoon")
}

*/

// Example 3. Using if-else Statements to check if a boolean value is true
/*
let isStudent = false;

if(isStudent){
    console.log("You are a student")
}
else{
    console.log("You are NOT a student")
}

*/

// Example 4. Using nested if Statements
/*
let age = 25;
let hasLicense = true;

if(age >= 16){
    console.log("You are old enough to drive");

    if(hasLicense){
        console.log("You have your License")
    }
    else{
        console.log("You don't have your license yet")
    }
}
else{
    console.log("You must be 16+ to have a license")
}

*/

// Example 5.
/*
let age = 101;

if(age >= 100){
    console.log("You are TO OLD to enter this site");
}
else if(age == 0){
    console.log("You can't enter. You were just born")
}
else if(age >=18){
    console.log("You are old enough to enter this site");
}
else if(age < 0){
    console.log("Your age can't be below 0");
}
else{
    console.log("You must be 18+ to endter this site");
}
*/

const myText = document.getElementById("myText");
const mySubmit = document.getElementById("mySubmit");
const resultElement = document.getElementById("resultElement");

let age = 0;

mySubmit.onclick = function(){

    age = myText.value;
    age = Number(age);

    if(age >= 100){
        resultElement.textContent = `You are TO OLD to enter this site`;
    }
    else if(age == 0){
        resultElement.textContent = `You can't enter. You were just born`
    }
    else if(age >=18){
        resultElement.textContent = `You are old enough to enter this site`
    }
    else if(age < 0){
        resultElement.textContent = `Your age can't be below 0`
    }
    else{
        resultElement.textContent = `You must be 18+ to endter this site`
    }
}





















