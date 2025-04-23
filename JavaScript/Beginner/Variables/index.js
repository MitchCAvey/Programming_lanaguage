
// Variable = A container that stores a value. Behaves as if it were the value it contains.

// 1. declaration       let x;
// 2. assignment        x = 100;

// let x;
// x = 100;

// console.log(x)

// let y = 125;

// console.log(y)


// let age = 25;
// let price = 10.56;
// let gpa = 2.5
// let student_name = "Mitch"

// console.log(age)

// console.log(price)

// console.log(gpa)

// console.log(student_name)

// console.log(`Your name is ${student_name}`)
// console.log(`Your age is ${age} years old. The price for a ticket is ${price}, but with a gpa of ${gpa}`)

// console.log(typeof age)
// console.log(typeof price)
// console.log(typeof gpa)
// console.log(typeof student_name)


// let online = true;
// let forSale = false;

// console.log(typeof online)

// console.log(`Mitch is online: ${online}`)
// console.log(`Is this car for sale? ${forSale}`)


let fullName = "Mitch Avey";
let age = 38;
let isStudent = false;

document.getElementById("p1").textContent = `Your name is ${fullName}`
document.getElementById("p2").textContent = `You are ${age} years old`
// document.getElementById("p3").textContent = `Are you a student ${isStudent}`
document.getElementById("p3").textContent = `Enrolled: ${isStudent}`