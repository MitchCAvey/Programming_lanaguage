

// While Loop = Repeat some code WHILE some condition is true
/*
let username = "";

if(username === ""){
    console.log(`You didn't enter your name!`);
}
else{
    console.log(`Hello ${username}`);
}
    */

//The below while-loop code will create in infinate loop
//As we have no way to get a username which will break the 
//the while-loop

/*
while(username === ""){
    console.log(`You didn't enter your name!`);
}

console.log(`Hello ${username}`);
*/

// By setting the username before getting to the while-loop
// we end up skipping over the while-loop, as the username now
// has a value of not Null
/*
let username2 = "MitchAvey";

while(username2 === ""){
    console.log(`You didn't enter your name!`);
}

console.log(`Hello ${username2}`);
*/

// Or we can provide a way when we are in the while-loop
// to provide a value for username.
/*
let username3 = "";

while(username3 === "" || username3 === null){
    // console.log(`You didn't enter your name!`);
    username3 = window.prompt(`Enter your username: `);
}

console.log(`Hello ${username3}`);
*/

// You can also use do-while-loops in JavaScript
/*
let username4;

do{
    // console.log(`You didn't enter your name!`);
    username4 = window.prompt(`Enter your username: `);
}while(username4 === "" || username4 === null)

console.log(`Hello ${username4}`);
*/

let loggedIn = false;
let username5;
let password;

while(!loggedIn){
    username5 = window.prompt(`Enter your username: `);
    password = window.prompt(`Enter your password: `);

    if(username5 === "myUsername" && password === "myPassword"){
        loggedIn = true;
        console.log("You are logged in now!");
    }
    else{
        console.log("Invalid credentials! Please try again")
    }
}

// Using a do-while-loop

let loggedIn1 = true;
let username6;
let password1;

do{
    username6 = window.prompt(`Enter your username: `);
    password1 = window.prompt(`Enter your password: `);

    if(username6 === "myUsername" && password1 === "myPassword"){
        loggedIn1 = true;
        console.log("You are logged in now!");
    }
    else{
        console.log("Invalid credentials! Please try again")
    }
}while(!loggedIn1)
