

/*
    this = reference to the object where THIS is used (the object depends on the immediate context)

        e.g. person.name = this.name;
*/


const person1 = {
    firstName: "Spongebob",
    lastName: "Squarepants",
    age: 30,
    isEmployed: true,
    favFood: "hanburgers",
    sayHello: function(){console.log(`Hi! I am ${this.firstName} ${this.lastName}`)},
    sayBye: function(){console.log("Goodbye")},
    eat: function(){console.log(`${this.firstName + " " + this.lastName} is eating ${this.favFood}`)}
};

const person2 = {
    firstName: "Patrick",
    lastName: "Star",
    favFood: "pizza",
    age: 42,
    isEmployed: false,
    sayHello: function(){console.log(`Hi! I am ${this.firstName + " " + this.lastName}!`)},
    sayBye: function(){console.log("Bye...")},
    eat: function(){console.log(`${this.firstName + " " + this.lastName} is eating ${this.favFood}`)}
};

person1.sayHello();
person1.eat();

person2.sayHello();
person2.eat();