
/*
    classList = Element property in JavaScript used to interact with an element's list
                of classes (CSS classes)
                Allows you to make reusable classes for many elements across your Webpage.
    
    1) add()
    2) remove()
    3) toggle (Remove if present, Add if not)
    4) replace(oldClass, newClass)
    5) contains()
*/

// Example 1
// const myBtn = document.getElementById("myBtn");

// Using add() and remove()
// myBtn.classList.add("enabled");
// myBtn.classList.remove("enabled");
// myBtn.classList.add("hover");

// myBtn.addEventListener("mouseover", event => {
//     event.target.classList.add("hover");
// });

// myBtn.addEventListener("mouseout", event => {
//     event.target.classList.remove("hover");
// });

//Exmaple 2
// Using toggle

// myBtn.addEventListener("mouseover", event => {
//     event.target.classList.toggle("hover");
// });

// myBtn.addEventListener("mouseout", event => {
//     event.target.classList.toggle("hover");
// });

// Example 3
// Using replace

// const myH1 = document.getElementById("myH1");
// const myBtn = document.getElementById("myBtn");

// myH1.classList.add("enabled")
// myBtn.classList.add("enabled");

// myBtn.addEventListener("click", event => {

//     if(event.target.classList.contains("disabled")){
//         event.target.textContent += "👌";
//     }
//     else{
//         event.target.classList.replace("enabled", "disabled");
//     }

    
// });

// myH1.addEventListener("click", event => {

//     if(event.target.classList.contains("disabled")){
//         event.target.textContent += "👌";
//     }
//     else{
//         event.target.classList.replace("enabled", "disabled");
//     }

    
// });

// Example 4
let buttons = document.querySelectorAll(".myBtns");

buttons.forEach(button => {
    button.classList.add("enabled");
});

// buttons.forEach(button => {
//     button.classList.remove("enabled");
// });

buttons.forEach(button => {
    button.addEventListener("mouseover", event => {
        event.target.classList.toggle("hover");
    });
});

buttons.forEach(button => {
    button.addEventListener("mouseout", event => {
        event.target.classList.toggle("hover");
    });
});

buttons.forEach(button => {
    button.addEventListener("click", event => {

        if(event.target.classList.contains("disabled")){
            event.target.textContent += "🤤";
        }
        else{
            event.target.classList.replace("enabled", "disabled");
        }

        // event.target.classList.replace("enabled", "disabled");
    });
});















