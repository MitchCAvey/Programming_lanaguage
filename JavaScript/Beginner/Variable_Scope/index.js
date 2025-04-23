

/*
    variable scope = Where a variable is recognized and accessible (local VS global)
*/


// let x = 1; // Global scope
let y = 6;

function function1(){
    let x = 1; // local scope
    console.log("Function 2");
    console.log(`Local Variable x = ${x}`);
    console.log(`Global Variable y = ${y}`);
}

function function2(){
    let x = 2; // local scope
    console.log("Function 2");
    console.log(`Local Variable x = ${x}`);
    console.log(`Global Variable y = ${y}`);
}

function function3(){
    console.log("Function 3");
    console.log(`Global Variable y = ${y}`);
}

function1();
function2();
function3();
















