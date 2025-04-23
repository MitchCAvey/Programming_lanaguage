
/*
    Async/Await = Async = makes a function return a promise
                  Await = makes an async function wait for a promise

                  Allows you write asynchronous code in a synchronous manner
                  Async doesn't have resolve or reject parameters
                  Everything after Await is placed in an event queue
*/

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


// walkDog().then(value => {console.log(value); return cleanKitchen()})
//          .then(value => {console.log(value); return takeTrashOut()})
//          .then(value => {console.log(value); console.log(`You've now completed all chores!`)})
//          .catch(error => {console.error(error)});

async function doChores(){

    try{
        const walkDogResult = await walkDog();
        console.log(walkDogResult);

        const cleanKitchenResult = await cleanKitchen();
        console.log(cleanKitchenResult);

        const takeTrashOutResult = await takeTrashOut();
        console.log(takeTrashOutResult);

        console.log(`You've now completed all chores!`);
    }
    catch(error){
        console.error(error);
    }

}

doChores();

















