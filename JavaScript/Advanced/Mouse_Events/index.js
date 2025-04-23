
/*
    eventListener = Listen for specific events to create interactive web pages
                    events: click, mouseover, mouseout
                    .addEventListener(event, callback);
*/

const myBox = document.getElementById('myBox');
const myBtn = document.getElementById('myBtn');

// function changeColor(event){
//     // console.log(event);
//     event.target.style.backgroundColor = "red";
//     event.target.textContent = "OUCH! 🤕";
// }

// myBox.addEventListener("click", changeColor);


// Using an anonymous function
// myBox.addEventListener("click", function(event){
//     event.target.style.backgroundColor = "red";
//     event.target.textContent = "OUCH! 🤕";    
// });

// Using an arrow function
/*
myBox.addEventListener("click", event =>{
    event.target.style.backgroundColor = "red";
    event.target.textContent = "OUCH! 🤕";    
});


myBox.addEventListener("mouseover", event => {
    event.target.style.backgroundColor = "yellow";
    event.target.textContent = "Don't Do It! 🤬";     
});

myBox.addEventListener("mouseout", event => {
    event.target.style.backgroundColor = "lightgreen";
    event.target.textContent = "Click Me 😆";     
});
*/

// Changing the button
/*
myBtn.addEventListener("click", event =>{
    event.target.style.backgroundColor = "red";
    event.target.textContent = "OUCH! 🤕";    
});



myBtn.addEventListener("mouseover", event => {
    event.target.style.backgroundColor = "yellow";
    event.target.textContent = "Don't Do It! 🤬";     
});

myBtn.addEventListener("mouseout", event => {
    event.target.style.backgroundColor = "lightgreen";
    event.target.textContent = "Click Me 😆";     
});
*/

myBtn.addEventListener("click", event =>{
    myBox.style.backgroundColor = "red";
    myBox.textContent = "OUCH! 🤕";    
});


myBtn.addEventListener("mouseover", event => {
    myBox.style.backgroundColor = "yellow";
    myBox.textContent = "Don't Do It! 🤬";     
});

myBtn.addEventListener("mouseout", event => {
    myBox.style.backgroundColor = "lightgreen";
    myBox.textContent = "Click Me 😆";     
});












