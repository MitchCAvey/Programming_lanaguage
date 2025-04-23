
/*
    Logical Operators = Used to combine or manipulate boolean values
                        (true or false)

                        AND = &&
                        OR  = ||
                        NOT = !
*/

const temp = 20;

if(temp > 0){
    console.log("The weather is GOOD");
}
else if(temp <= 30){
    console.log("The weather is GOOD");
}
else{
    console.log("The weather is BAD")
}

// Using the AND Logical Operator
const temp2 = 40;

if(temp2 > 0 && temp2 <= 30){
    console.log("The weather is GOOD");
}
else{
    console.log("The weather is BAD")
}

// Using the OR Logical Operator
const temp3 = 20;

if(temp3 <= 0 || temp3 > 30){
    console.log("The weather is BAD");
}
else{
    console.log("The weather is GOOD")
}

// Using the OR Logical Operator
const isSunny = false;

if(!isSunny){
    console.log("It is CLOUDY");
}
else{
    console.log("It is SUNNY");
}
