

/*
    rest parameters = (...rest) allows a function to work with a variable number of 
                      arguments by bundling them into an array
    
    spread = Expands an array into seperate elements
    rest   = bundles seperate elements into an array
*/

const food1 = "pizza";
const food2 = "hamburger";
const food3 = "hotdog";
const food4 = "sushi";
const food5 = "ramen";

function openFridge(...foods){
    console.log(foods);
    console.log(...foods);
}

function getFood(...foods){
    return foods;
}

openFridge(food1, food2, food3, food4, food5);

const foods = getFood(food1, food2, food4);

console.log(foods);


function sum(...numbers){

    let result = 0;

    for(let n of numbers){
        result += n;
    }
    return result;
}

const total = sum(4,8,9);

console.log(total);

function getAverage(...numbers){

    let result = 0;

    for(let n of numbers){
        result += n;
    }
    return result / numbers.length;
}

const average = getAverage(75,100,85,90,50);
console.log(`The average is: ${average}`);

function combineString(...strings){
    return strings.join(" ");
}

const fullName = combineString("Mr.", "Spongebob", "Squarepants", "III");

console.log(fullName);













