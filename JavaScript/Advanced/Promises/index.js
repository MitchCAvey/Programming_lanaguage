
/*
    Promise = An Object that manages asynchronous operations.
              Wrap a Promise Object around {asynchrounus code}
              "I promise to return a value"
              PENDING -> RESOLVED or REJECTED
              new Promise((resolve, reject) => {asynchronous code})
    
    DO THESE CHORES IN ORDER

    1. WALK THE DOG
    2. CLEAN THE KITCHEN
    3. TAKE OU THE TRASH
*/

// Example 1
// function walkDog(callback){

//     setTimeout(() => {
//         console.log(`You walk the dog 🐕‍🦺`);
//         callback();
//     }, 1500);
// }

// function cleanKitchen(callback){

//     setTimeout(() => {
//         console.log(`You cleaned the kitchen 🧹`);
//         callback();
//     }, 2500);
// }

// function takeTrashOut(callback){

//     setTimeout(() => {
//         console.log(`You took out the trash 🗑️🚮`);
//         callback();
//     }, 500)
// }


// walkDog(() => {
//     cleanKitchen(() => {
//         takeTrashOut(() => console.log(`You've now completed all chores!`));
//     });
// });


function walkDog(){

    return new Promise((resolve, reject) => {
        setTimeout(() => {

            const dogwalked = true;

            if(dogwalked){
                resolve(`You walk the dog 🐕‍🦺`);
            }
            else{
                reject(`You didn't walk the dog!`);
            }
        }, 1500);
    });
}

function cleanKitchen(){

    return new Promise((resolve, reject) => {
        setTimeout(() => {
            
            const cleanedkitchen = true;

            if(cleanedkitchen){
                resolve(`You cleaned the kitchen 🧹`);
            }
            else{
                reject(`You didn't clean the kitchen!`);
            }
        }, 2500);
    });
}

function takeTrashOut(){

    return new Promise((resolve, reject) => {
        setTimeout(() => {
            
            const trashIsOut = true;

            if(trashIsOut){
                resolve(`You took out the trash 🗑️🚮`);
            }
            else{
                reject(`You didn't take the trash out!`);
            }

        }, 500);
    });
}

// walkDog().then(value => {console.log(value); return cleanKitchen()}).then(value => console.log(value));

walkDog().then(value => {console.log(value); return cleanKitchen()})
         .then(value => {console.log(value); return takeTrashOut()})
         .then(value => {console.log(value); console.log(`You've now completed all chores!`)})
         .catch(error => {console.error(error)});










