
/*
    NodeList = Static collection of HTML elements by (id, class, element)
                Can be created by using querySelectorAll()
                Similar to an array, but no (map, filer, reduce) but do have
                a forEach() method
                NodeList won't update to automatically reflect changes
*/

let buttons = document.querySelectorAll(".myBtns");

console.log(buttons);

// Example 1
// ADD HTML/CSS PROPERTIES

// buttons.forEach(button => {
//     button.style.backgroundColor = "green";
//     button.textContent += "😎😆";
// });

//Example 2
// CLICK event listener

// buttons.forEach(button => {
//     button.addEventListener("click", event => {
//         event.target.style.backgroundColor = "tomato";
//     });
// });

// Example 3
// MOUSEOVER + MOUSEOUT event listener

// buttons.forEach(button => {
//     button.addEventListener("mouseover", event => {
//         event.target.style.backgroundColor = "darkblue";
//     });
// });

// buttons.forEach(button => {
//     button.addEventListener("mouseout", event => {
//         event.target.style.backgroundColor = "hsl(205, 100%, 60%)";
//     });
// });

// Example 3
// ADD AN ELEMENT

// const newBtn = document.createElement("button"); // STEP 1

// newBtn.textContent = "Button 5"; //STEP 2
// newBtn.classList = "myBtns";

// document.body.appendChild(newBtn); // STEP 3

// // console.log(buttons);

// buttons = document.querySelectorAll(".myBtns");

// console.log(buttons);

// Example 4
// REMOVE AN ELEMENT

buttons.forEach(button => {
    button.addEventListener("click", event => {
        event.target.remove();
        // console.log(buttons);
        buttons = document.querySelectorAll(".myBtns");
        console.log(buttons);
    });
});




















