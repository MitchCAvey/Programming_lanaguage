
/*
    setTimeout() = function in JavaScript that allows you to Schedule the execution of a function
                    after an amount of time (milliseconds). Times are approximate
                    (varies based on the workload of the JavaScript runtime env.)

                    setTimeout(callback, delay);
*/

// Example 1
/*
function sayHellow(){
    window.alert("Hello");
}

setTimeout(sayHellow, 3000);
*/

// Example 2
/*
setTimeout(function(){window.alert("Hello")}, 3000);
*/

// Example 3
/*
const timeoutID = setTimeout(() => window.alert("Hello"), 3000);

clearTimeout(timeoutID);

*/

// Example 4: Using a botton in HTML

let timeoutID;

function startTimer(){
    timeoutID = setTimeout(() => window.alert("Hello"), 3000);
    console.log("STARTED")
}

function clearTimer(){
    clearTimeout(timeoutID);
    console.log("CLEARED");
}










