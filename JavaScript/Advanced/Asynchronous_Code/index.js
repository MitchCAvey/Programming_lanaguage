
/*
    Synchronous = Executes line by line consecutively in a sequential manner
                    Code that waits for an operation to complete. 
    
    Asynchronous = Allows multiple operations to be performed concurrently without waiting 
                    Doesn't block the execution flow and allows the program to continue
                    (I/O operations, network requests, fetching data)
                    Handled with: Callbacks, Promises, Async/Await
*/

// console.log(`Taks 1`);
// console.log(`Taks 2`);
// console.log(`Taks 3`);

function func1(callback){
    setTimeout(() => {console.log("Task 1"); callback()}, 3000);
}

function func2(){
    console.log(`Taks 2`);
    console.log(`Taks 3`);
    console.log(`Taks 4`);

}

func1(func2);

















