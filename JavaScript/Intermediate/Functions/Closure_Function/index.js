

/*
    closure = A function defined inside of another function, the inner function has access to 
    the variables and scope of the outer function.
    Allow for private variables and state maintenance
    Used frequently in JS frameworks: React, Vue, Angular
*/


// Example 1: The basic idea
function outer(){

    let message = "Hello";

    function inner(){
        console.log(message);
    }

    inner();
}

outer();


//Example 2:

function createCounter(){

    let count = 0;

    function increment(){

        // let count = 0;
        count++;
        console.log(`Count increased to ${count}`);
    }

    function getCount(){
        return count;
    }

    return {increment:increment, getCount:getCount};
    // return {increment}; // Short hande version of above
}

const counter = createCounter();

counter.increment();
counter.increment();
counter.increment();
counter.increment();

console.log(`The current count is ${counter.getCount()}`)


//Example 3: Playing a game
/*
let score = 0;

function increasedScore(points){
    score += points;
    console.log(`+${points}pts`)
}

function decreasedScore(points){
    score -= points;
    console.log(`-${points}pts`)
}

function getScore(){
    return score;
}

increasedScore(5);
increasedScore(6);
decreasedScore(3);

console.log(`THe final score is ${getScore()}pts`);

*/

function createGame(){
    let score = 0;

    function increasedScore(points){
        score += points;
        console.log(`+${points}pts`)
    }

    function decreasedScore(points){
        score -= points;
        console.log(`-${points}pts`)
    }

    function getScore(){
        return score;
    }

    return {increasedScore, decreasedScore, getScore};
}

const game = createGame();

game.increasedScore(5);
console.log(game.getScore());
game.increasedScore(6);
console.log(game.getScore());
game.decreasedScore(3);
console.log(game.getScore());














