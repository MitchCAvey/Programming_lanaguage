

// String Methods = Allow you to manipulate and work with text (strings)

let userName = " MitchAvey";


// userName.charAt(0);
console.log(userName.charAt(5));

console.log(userName.indexOf("A"));

console.log(userName.lastIndexOf("A"));

console.log(userName.length);

userName = userName.trim();

console.log(userName)

userName = userName.toUpperCase();

console.log(userName)

userName = userName.toLowerCase();

console.log(userName)

userName = userName.repeat(2);

console.log(userName);



let userName2 = "MitchAvey";
let result = userName2.startsWith(" ");

console.log(result);


if(result){
    console.log("Your username can't begin with ' '")
}
else{
    console.log(userName2);
}

let userName3 = "MitchAvey ";
let result2 = userName3.endsWith(" ");

console.log(result2);


if(result2){
    console.log("Your username can't begin with ' '")
}
else{
    console.log(userName3);
}


let userName4 = "Mitch Avey ";
let result3 = userName4.includes(" ");

console.log(result3);


if(result3){
    console.log("Your username can't begin with ' '")
}
else{
    console.log(userName4);
}


let phoneNumber = "568-458-3221"

console.log(phoneNumber)

phoneNumber = phoneNumber.replaceAll('-', '');

console.log(phoneNumber);

let phoneNumber1 = "568-458-3221"

console.log(phoneNumber1)

phoneNumber1 = phoneNumber1.padStart(15, "0");

console.log(phoneNumber1);

let phoneNumber2 = "568-458-3221"

console.log(phoneNumber2)

phoneNumber2 = phoneNumber2.padEnd(15, "0");

console.log(phoneNumber2);