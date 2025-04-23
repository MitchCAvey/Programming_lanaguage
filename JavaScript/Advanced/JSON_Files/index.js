

/*
    JSON = (JavaScript Object Notation) data-interchange format used for exchanging
            data between a server and a web application. JSON files {key:value} OR
            [value1, value2, value3], OR [{}, {}, {}]
    
    JSON.stringify() = converts a JS object to a JSON string.
    JSON.parse() = converts a JSON string to a JS object
*/

// Example 1

// const names = ["Spongebob", "Patrick", "Squadward", "Sandy"];
// const person = {"name": "Spongebob", "age": 30, "isEmployed": true, 
//                 "hobbies": ["jellyfishing", "Karate", "Cooking"]};

// const people = [{"name": "Spongebob", "age": 30, "isEmployed": true},
//                 {"name": "Patrick", "age": 34, "isEmployed": true},
//                 {"name": "Squadward", "age": 50, "isEmployed": true},
//                 {"name": "Mr.Puff", "age": 45, "isEmployed": true}];

// const jsonString = JSON.stringify(names);

// console.log(names);
// console.log(jsonString);

// const jsonString1 = JSON.stringify(person);

// console.log(person);
// console.log(jsonString1);

// const jsonString2 = JSON.stringify(people);

// console.log(people);
// console.log(jsonString2);

// Exmaple 2
// const jsonNames = `["Spongebob", "Patrick", "Squadward", "Sandy"]`;
// const jsonPerson = `{"name": "Spongebob", "age": 30, "isEmployed": true, 
//                     "hobbies": ["jellyfishing", "Karate", "Cooking"]}`;

// const jsonPeople = `[{"name": "Spongebob", "age": 30, "isEmployed": true},
//                     {"name": "Patrick", "age": 34, "isEmployed": true},
//                     {"name": "Squadward", "age": 50, "isEmployed": true},
//                     {"name": "Mr.Puff", "age": 45, "isEmployed": true}]`;

// console.log(jsonNames);
// const parsedData = JSON.parse(jsonNames);
// console.log(parsedData);

// console.log(jsonPerson);
// const parsedData1 = JSON.parse(jsonPerson);
// console.log(parsedData1);

// console.log(jsonPeople);
// const parsedData2 = JSON.parse(jsonPeople);
// console.log(parsedData2);

// Example 3

// fetch("./person.json")
//     .then(response => response.json())
//     .then(value => console.log(value));

// fetch("./people.json")
//     .then(response => response.json())
//     .then(value => console.log(value));

// fetch("./names.json")
//     .then(response => response.json())
//     .then(value => console.log(value));

fetch("person.json")
    .then(response => response.json())
    .then(values => console.log(values))
    .catch(error => console.error(error));

fetch("people.json")
    .then(response => response.json())
    .then(values => values.forEach(value => console.log(value)))
    .catch(error => console.error(error));

fetch("people.json")
    .then(response => response.json())
    .then(values => values.forEach(value => console.log(value.name)))
    .catch(error => console.error(error));

fetch("people.json")
    .then(response => response.json())
    .then(values => values.forEach(value => console.log(value.age)))
    .catch(error => console.error(error));

// fetch("names.json")
//     .then(response => response.json())
//     .then(values => values.forEach(value => console.log(value)))
//     .catch(error => console.error(error));











