
// ---------------- Example 1 <h1> ----------------

// STEP 1 CREATE THE ELEMENT
const newH1 = document.createElement("h1");
const newListItem = document.createElement("li");

// STEP 2 ADD ATTRIBUTES/PROPERTIES
newH1.textContent = "I like Pizza!";
newH1.id = "myh1";
newH1.style.color = "tomato";
newH1.style.textAlign = "center";

newListItem.textContent = "coconut";
newListItem.id = "coconut";
newListItem.style.fontWeight = "bold";
newListItem.style.backgroundColor = "lightgreen";


// STEP 3 APPEND ELEMENT TO DOM
// document.body.append(newH1);
// document.body.prepend(newH1);
document.getElementById("box1").append(newH1);
// document.getElementById("box1").prepend(newH1);

// Exmaple 2

// const box1 = document.getElementById("box1");
// document.body.insertBefore(newH1, box1);

// const box2 = document.getElementById("box2");
// document.body.insertBefore(newH1, box2);

// const box3 = document.getElementById("box3");
// document.body.insertBefore(newH1, box3);

// const boxes = document.querySelectorAll(".box");
// document.body.insertBefore(newH1, boxes[0]);
// document.body.insertBefore(newH1, boxes[1]);
// document.body.insertBefore(newH1, boxes[3]);

//Example 3

// document.body.append(newListItem);
// document.body.prepend(newListItem);
document.getElementById("fruits").append(newListItem);
// document.getElementById("fruits").prepend(newListItem);

// const orange = document.getElementById("orange");
// document.getElementById("fruits").insertBefore(newListItem, orange);

// const banana = document.getElementById("banana");
// document.getElementById("fruits").insertBefore(newListItem, banana);

// const listItems = document.querySelectorAll("#fruits li");
// document.getElementById("fruits").insertBefore(newListItem, listItems[0]);
// document.getElementById("fruits").insertBefore(newListItem, listItems[1]);


// REMOVE HTML ELEMENT

// document.body.removeChild(newH1);
// document.getElementById("box1").removeChild(newH1);
document.getElementById("fruits").removeChild(newListItem);





