

/*
    callback = A function that is passed as an argument to another function. 

               Used to handle asynchronous operations:
               1. Reading a file
               2. Network requests
               3. Interacting with databases

               "Hey, when you're done, call this next"
*/

function hello(callback){
    console.log("Hello!");
    callback();
}

function hello2(){
    setTimeout(function(){
        console.log("Hello!");
    }, 3000);
}

function goodBye(){
    console.log("Goodbye!");
}

function leave(){
    console.log("Leave!");
}

function wait(){
    console.log("Wait!");
}

/*
    make sure to not include the '()' as it will call the function right away. 
    By not including the '()' you have created a callback
*/
// hello(goodBye);
// hello(leave);
hello(wait);

// hello2();
// goodBye();


// Example 2

function sum(callback, x, y){
    let result = x + y;
    callback(result);
}

function displayConsole(result){
    console.log(result);
}

function displayPage(result){
    document.getElementById("myH1").textContent = result;
}

// sum(displayConsole, 1, 2);
sum(displayPage, 1, 2);


