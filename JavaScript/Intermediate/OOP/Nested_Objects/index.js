

/*
    nested objects = Objects inside of other Objects. Allows you to represent more complex data 
                     structures. Child Object is enclosed by a Parent Object

                     Persion{Address{}, ContactInfo{}}
                     ShoppingCart{Keyboard{}, Mouse{}, Monitor{}}
*/


// example 1
/*
const person = {
    fullName: "Spongbob Squarepants",
    age: 30,
    isStudent: true,
    hobbies: ["karate", "Jellyfishing", "cooking"],
    address: {
        street: "124 Conch St.",
        city: "Bikini Bottom",
        country: "Int. Water"
    }
}


console.log(`${person.fullName}`);
console.log(`${person.age}`);
console.log(`${person.isStudent}`);
console.log(`${person.hobbies}`);
console.log(`${person.hobbies[0]}`);
console.log(`${person.hobbies[1]}`);
console.log(`${person.hobbies[2]}`);
console.log(person.address);
console.log(`${person.address.street}`);
console.log(`${person.address.city}`);
console.log(`${person.address.country}`);

// Looping through a nested object

for(const property in person.address){
    console.log(person.address[property]);
}
*/

//Example 2

class Address{
    constructor(street, city, country){
        this.street = street;
        this.city = city;
        this.country = country;
    }
}

class Person{
    constructor(name, age, ...address){
        this.name = name;
        this.age = age;
        this.address = new Address(...address);
    }
}

const person1 = new Person("Spongebob", 30, "123 Conch St.", "Bikini Bottom", "Int. Waters");
const person2 = new Person("Patrick", 37, "127 Conch St.", "Bikini Bottom", "Int. Waters");
const person3 = new Person("Squidward", 45, "125 Conch St.", "Bikini Bottom", "Int. Waters");

console.log(`Person 1`);
console.log(`First Name: ${person1.name}`);
console.log(`Age: ${person1.age}`);
console.log(`Address: ${person1.address.street}`);
console.log(`City: ${person1.address.city}`);
console.log(`Country: ${person1.address.country}`);
// console.log(person1.address);

console.log(`Person 2`);
console.log(`First Name: ${person2.name}`);
console.log(`Age: ${person2.age}`);
console.log(`Address: ${person2.address.street}`);
console.log(`City: ${person2.address.city}`);
console.log(`Country: ${person2.address.country}`);

console.log(`Person 3`);
console.log(`First Name: ${person3.name}`);
console.log(`Age: ${person3.age}`);
console.log(`Address: ${person3.address.street}`);
console.log(`City: ${person3.address.city}`);
console.log(`Country: ${person3.address.country}`);

