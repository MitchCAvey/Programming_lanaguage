

/*
    Element selectors = Methods used to target and manipulate HTML elements
                        They allow you to select one or multiple HTML elements
                        from the DOM (Document Object Model)
        
    1. document.getElementById() ==============> Element or Null
    2. document.getElementsClassName() ========> HTML Collection
    3. document.getElementsByTagName() ========> HTML Collection
    4. document.querySelector() ===============> Element Or Null
    5. document.querySelectorAll() ============> Nodelist
*/

const myHeading = document.getElementById("my-heading");
myHeading.style.backgroundColor = "yellow";
myHeading.style.textAlign = "center";

console.log(myHeading);

// Example 2

const fruits = document.getElementsByClassName("fruits");

// console.log(fruits);

// fruits[0].style.backgroundColor = "yellow";
/*
for(let fruit of fruits){
    fruit.style.backgroundColor = "yellow";
}
*/
// fruits.forEach();

// Array.from(fruits).forEach(fruit => {fruit.style.backgroundColor = "yellow"});

// Example 3

const h4Elements = document.getElementsByTagName("h4");
const liElements = document.getElementsByTagName("li");

// console.log(h4Elements);

// h4Elements[0].style.backgroundColor = "yellow";

// h4Elements[1].style.backgroundColor = "yellow";

/*
for(let h4Element of h4Elements){
    h4Element.style.backgroundColor = "yellow";    
}

for(let liElement of liElements){
    liElement.style.backgroundColor = "lightgreen";
}
*/

/*
Array.from(h4Elements).forEach(h4Element => {
    h4Element.style.backgroundColor = "yellow";
});

Array.from(liElements).forEach(liElement => {
    liElement.style.backgroundColor = "lightgreen";
});
*/

// Example 4

// You can select either a class or a tag
// const element = document.querySelector("ul");

// element.style.backgroundColor = "Yellow";

// Example 5

const fruits1 = document.querySelectorAll(".fruits");
const foods = document.querySelectorAll("li");

fruits1[0].style.backgroundColor = "yellow";
fruits1[1].style.backgroundColor = "yellow";
fruits1[2].style.backgroundColor = "yellow";

// foods[0].style.backgroundColor = "purple";
// foods[1].style.backgroundColor = "purple";
// foods[2].style.backgroundColor = "purple";

foods.forEach(food => {
    food.style.backgroundColor = "purple"
});












