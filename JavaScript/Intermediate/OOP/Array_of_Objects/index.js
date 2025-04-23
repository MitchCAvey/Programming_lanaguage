

const fruits = [
    {name: "Apple", color:"Red", calories: 95},
    {name: "Orange", color:"Orange", calories: 45},
    {name: "Banana", color:"Yellow", calories: 105},
    {name: "Coconut", color:"White", calories: 159},
    {name: "Pineapple", color:"Yellow", calories: 37}
];


console.log(fruits[0].name);
console.log(fruits[0].color);
console.log(fruits[0].calories);

console.log(fruits[1].name);
console.log(fruits[1].color);
console.log(fruits[1].calories);

console.log(fruits[2].name);
console.log(fruits[2].color);
console.log(fruits[3].calories);

console.log(fruits[3].name);
console.log(fruits[3].color);
console.log(fruits[3].calories);

console.log(fruits[4].name);
console.log(fruits[4].color);
console.log(fruits[4].calories);

console.log(fruits);

fruits.push({name: "Grapes", color: "Purple", calories: 62});

console.log(fruits[5].name);
console.log(fruits[5].color);
console.log(fruits[5].calories);

console.log(fruits);

// fruits.pop();

// console.log(fruits);

// fruits.splice(1, 2);

// console.log(fruits);

// ----------- forEach() -------------

fruits.forEach(fruit => console.log(fruit));

fruits.forEach(fruit => console.log(fruit.name));

// ----------- map() ------------------

const fruitNames = fruits.map(fruit => fruit.name);
const fruitColors = fruits.map(fruit => fruit.color);
const fruitCalories = fruits.map(fruit => fruit.calories);

console.log(fruitNames);
console.log(fruitColors);
console.log(fruitCalories);

// ----------- filter() -------------

const yellowFruits = fruits.filter(fruit => fruit.color === "Yellow");
const lowCalFruits = fruits.filter(fruit => fruit.calories < 100);
const highCalFruits = fruits.filter(fruit => fruit.calories > 100);

console.log(yellowFruits);
console.log(lowCalFruits);
console.log(highCalFruits);

// ----------- reduce() -------------

// const maxFruitCal = fruits.reduce(accumulator, element)
const maxFruitCal = fruits.reduce((max, fruit1) => fruit1.calories > max.calories ? fruit1 : max);
const minFruitCal = fruits.reduce((min, fruit2) => fruit2.calories < min.calories ? fruit2 : min);

console.log(maxFruitCal);
console.log(minFruitCal);