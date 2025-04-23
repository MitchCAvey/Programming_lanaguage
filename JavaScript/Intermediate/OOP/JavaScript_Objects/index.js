
/* 
    Object = A collection of related properties and/or methods. 
             Can represent real world objects (people, products, places)

        e.g. object = {key:value,
                       function()}
*/


const person1 = {
    firstName: "Spongebob",
    lastName: "Squarepants",
    age: 30,
    isEmployed: true,
    sayHello: function(){console.log("Hi! I am Spongebob!")},
    sayBye: function(){console.log("Goodbye")},
    eat: function(){console.log(`I am eating a Krabby Patty`)}
};

const person2 = {
    firstName: "Patrick",
    lastName: "Star",
    age: 42,
    isEmployed: false,
    sayHello: function(){console.log("Hi! I am Patrick!")},
    sayBye: function(){console.log("Bye...")},
    eat: function(){console.log(`I am eating a roast beef, chicken, and pizza`)}
};


console.log("Person 1:")
console.log(person1.firstName);
console.log(person1.lastName);
console.log(person1.age);
console.log(person1.isEmployed);
person1.sayHello();
person1.sayBye();
person1.eat();
console.log("Person 2:");
console.log(person2.firstName);
console.log(person2.lastName);
console.log(person2.age);
console.log(person2.isEmployed);
person2.sayHello();
person2.sayBye();
person2.eat();















