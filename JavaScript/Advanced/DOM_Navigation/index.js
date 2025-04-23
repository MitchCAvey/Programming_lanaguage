

/*
    DOM Navigation = The process of navigating through the structure of
                     an HTML document using JavaScript
    
    1) .firstElementChild
    2) .lastElementChild
    3) .nextElementSibling
    4) .previousElementSibling
    5) .parentElement
    6) .children
*/


//Example 1 ------------ .firstElementChild ------------

// const element = document.getElementById("fruits");
// const element = document.getElementById("vegetables");
// const element = document.getElementById("desserts");
// const firstChild = element.firstElementChild;
// firstChild.style.backgroundColor = "yellow";
/*
const ulElements = document.querySelectorAll("ul");

ulElements.forEach(ulElement => {
    const firstChild = ulElement.firstElementChild;
    firstChild.style.backgroundColor = "yellow";
})
*/

//Example 2 ------------ .lastElementChild ------------

// const element = document.getElementById("fruits");
// const element = document.getElementById("vegetables");
// const element = document.getElementById("desserts");
// const lastChild = element.lastElementChild;

// lastChild.style.backgroundColor = "yellow";
/*
const ulElements = document.querySelectorAll("ul");

ulElements.forEach(ulElement => {
    const lastChild = ulElement.lastElementChild;
    lastChild.style.backgroundColor = "yellow";
})

*/

//Example 3 ------------ .nextElementSibling ------------

// const element = document.getElementById("apple");
// const element = document.getElementById("carrots");
// const element = document.getElementById("cake");
// const element = document.getElementById("fruits");
// const nextSibling = element.nextElementSibling;
// nextSibling.style.backgroundColor = "yellow";

//Example 4 ------------ .previousElementSibling ------------

// const element = document.getElementById("orange");
// const element = document.getElementById("banana");
// const element = document.getElementById("onions");
// const element = document.getElementById("icecream");
// const element = document.getElementById("vegetables");
// const element = document.getElementById("desserts");
// const prevSibling = element.previousElementSibling;
// prevSibling.style.backgroundColor = "yellow";

//Example 5 ------------ .parentElement ------------

// const element = document.getElementById("apple");
// const element = document.getElementById("potatoes");
// const element = document.getElementById("icecream");
// const parent = element.parentElement;
// parent.style.backgroundColor = "yellow";

//Example 6 ------------ .children ------------

// const element = document.getElementById("fruits");
// const element = document.getElementById("vegetables");
const element = document.getElementById("desserts");
const children = element.children;

// console.log(children);

// children[0].style.backgroundColor = "yellow";
// children[1].style.backgroundColor = "yellow";
// children[2].style.backgroundColor = "yellow";

Array.from(children).forEach(child => {
    child.style.backgroundColor = "yellow";
})












