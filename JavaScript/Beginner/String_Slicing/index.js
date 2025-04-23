

/*
    String Slicing = Creating a substring from a portion of another string

                     e.g. string.slice(start, end);
*/

const fullName = "Mitchell Avey";

let firstName = fullName.slice(0, 8);
let lastName = fullName.slice(9, 13);

let firstChar = fullName.slice(0, 1);
let lastChar = fullName.slice(-1);

console.log(`Your first name is: ${firstName}`);
console.log(`Your last name is: ${lastName}`);
console.log(`The first charater in your name is: ${firstChar}`);
console.log(`The last charater in your name is: ${lastChar}`);

const fullName1 = "Mitchell Avey";

let firstName2 = fullName1.slice(0, fullName1.indexOf(" "));
let lastName2 = fullName1.slice(fullName1.indexOf(" ") + 1);

console.log(`Your first name is: ${firstName2}`);
console.log(`Your last name is: ${lastName2}`);


const email = "MitchAvey@acme.com";

let userName3 = email.slice(0, email.indexOf("@"));
let extension = email.slice(email.indexOf("@") + 1);

console.log(`Your Username based on your email is: ${userName3}`);
console.log(`Your Email extension is: ${extension}`);
