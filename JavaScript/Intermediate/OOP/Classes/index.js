

/*
    class = (ES6 feature) provides a more structured and clean way to work with objects compared to
            traditional constructor functions ex. static keyword, encapsulation, inheritance
*/

/*
function Product(name, price){

    this.name = name;
    this.price = price;

    this.displayProduct = function(){
        console.log(`Product: ${this.name}`);
        console.log(`Price: $${this.price.toFixed(2)}`);
    };

    this.calculateTotal = function(salesTax){
        return this.price + (this.price * salesTax);
    }
}

const salesTax = 0.05;
const product1 = new Product("Shirt", 19.99);
const product2 = new Product("Pants", 22.50);
const product3 = new Product("Underwear", 100.00);

product1.displayProduct();

const totalPrice = product1.calculateTotal(salesTax);

console.log(`Total Price (with tax): $${totalPrice.toFixed(2)}`);

*/

// Using a class to simplify the above

class Product1{
    constructor(name, price){
        this.name = name;
        this.price = price;
    }

    displayProduct1(){
        console.log(`Product: ${this.name}`);
        console.log(`Price: $${this.price.toFixed(2)}`);
    }

    calculateTotal(salesTax){
        return this.price + (this.price * salesTax)
    }
}

const product1 = new Product1("Shirt", 19.99);
const product2 = new Product1("Pants", 22.50);
const product3 = new Product1("Underwear", 100.00);

const salesTax = 0.05;

product1.displayProduct1();
product2.displayProduct1();
product3.displayProduct1();

const total1 = product1.calculateTotal(salesTax);

console.log(`Total price (with tax): $${total1.toFixed(2)}`);

const total2 = product2.calculateTotal(salesTax);

console.log(`Total price (with tax): $${total2.toFixed(2)}`);

const total3 = product3.calculateTotal(salesTax);

console.log(`Total price (with tax): $${total3.toFixed(2)}`);









