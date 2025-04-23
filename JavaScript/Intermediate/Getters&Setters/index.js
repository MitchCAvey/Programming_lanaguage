

/*
    getter = Special method that makes a property readable
    setter = Special method that makes a property writeable

    validate and modify a value when reading/writing a property
*/

// Example 1
/*
class Rectangle{

    constructor(width,height){
        this.width = width;
        this.height = height;
    }

    set width(newWidth){
        if(newWidth > 0){
            this._width = newWidth;
        }
        else{
        console.error("Width must be a positive number");
        }
    }

    set height(newHeight){
        if(newHeight > 0){
            this._height = newHeight;
        }
        else{
            console.error("Height must be a positive number");
        }
    }

    get width(){
        return `${this._width.toFixed(1)}cm`;
    }

    get height(){
        return `${this._height.toFixed(1)}cm`;
    }

    get area(){
        return `${(this._width * this._height).toFixed(1)}cm^2`;
    }
}


// const rectangle = new Rectangle(-1000000, "pizza");
// const rectangle = new Rectangle(-1000000, "pizza");

const rectangle = new Rectangle(3, 4);

rectangle.width = 5;
rectangle.height = 6;


console.log(`Width: ${rectangle.width}, Height: ${rectangle.height}`);
console.log(`Area: ${rectangle.area}`);

*/

// Example 2

class Person{

    constructor(firstName, lastName, age){
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
    }

    set firstName(newFirstName){
        if(typeof newFirstName === "string" && newFirstName.length > 0){
            this._firstName = newFirstName;
        }
        else{
            console.error(`First name must be a non-empty string`);
        }
    }

    set lastName(newLastName){
        if(typeof newLastName === "string" && newLastName.length > 0){
            this._lastName = newLastName;
        }
        else{
            console.error(`First name must be a non-empty string`);
        }
    }

    set age(newAge){
        if(typeof newAge === "number" && newAge >= 0){
            this._age = newAge;
        }
        else{
            console.error(`Age must be a non-negative number`);
        }
    }

    get firstName(){
       return this._firstName; 
    }

    get lastName(){
        return this._lastName; 
     }

     get age(){
        return this._age; 
     }

     get fullName(){
        return this._firstName + " " + this._lastName;
     }
}

const person = new Person("Spongebob", "Squarepants", 39);

console.log(`First Name: ${person.firstName}`);
console.log(`Last Name: ${person.lastName}`);
console.log(`Full Name: ${person.fullName}`);
console.log(`Age: ${person.age}`);




