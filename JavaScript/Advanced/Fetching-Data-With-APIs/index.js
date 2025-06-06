

/*
    fetch = Is a function used for making HTTP requests to fetch resources.
            (JSON style data, images, files)
            Simplifies asynchronous data fetching in JavaScript and 
            used for interacting with APIs to retrieve and send
            data asynchronously over the web. 

            fetch(url, {options})
            fetch(url, {method: "GET", "POST", "PUT", "DELETE"})
*/

// Example 1
// fetch("https://pokeapi.co/api/v2/pokemon/pikachu")
//     .then(response => console.log(response))
//     .catch(error => console.error(error));

// fetch("https://pokeapi.co/api/v2/pokemon/pikachu")
//     .then(response => response.json())
//     .then(data => console.log(data))
//     .catch(error => console.error(error));

// fetch("https://pokeapi.co/api/v2/pokemon/pikachu")
//     .then(response => response.json())
//     .then(data => console.log(data.weight))
//     .catch(error => console.error(error));

// fetch("https://pokeapi.co/api/v2/pokemon/pikachu")
//     .then(response => {

//         if(!response.ok){
//             throw new Error("Could not fetch resource");
//         }
//         return response.json();
//     })
//     .then(data => console.log(data.stats))
//     .catch(error => console.error(error));

// Example 2

// async function fetchData(){

//     try{
//         const response = await fetch("https://pokeapi.co/api/v2/pokemon/typhlosion")

//         if(!response.ok){
//             throw new Error("Could not fetch resource");
//         }

//         const data = await response.json();
//         console.log(data);
//     }
//     catch(error){
//         console.error(error);
//     }
// }

// async function fetchData(){

//     try{

//         const pokemonName = document.getElementById("pokemonName").value.toLowerCase();
//         const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonName}`)

//         if(!response.ok){
//             throw new Error("Could not fetch resource");
//         }

//         const data = await response.json();
//         console.log(data);
//     }
//     catch(error){
//         console.error(error);
//     }
// }

async function fetchData(){

    try{

        const pokemonName = document.getElementById("pokemonName").value.toLowerCase();
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonName}`)

        if(!response.ok){
            throw new Error("Could not fetch resource");
        }

        const data = await response.json();
        // console.log(data);
        const pokemonSprite = data.sprites.front_default;
        const imgElement = document.getElementById("pokemonSprite");

        imgElement.src = pokemonSprite;
        imgElement.style.display = "block";
    }
    catch(error){
        console.error(error);
    }
}


// async function fetchData(){
    
//     try{

//         const pokemonName = document.getElementById("pokemonName").value.toLowerCase();
//         const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonName}`);

//         if(!response.ok){
//             throw new Error("Could not fetch resource");
//         }
        
//         const data = await response.json();
//         // console.log(data);
//         const pokemonSprite = data.sprites.front_default;
//         const imgElement = document.getElementById("pokemonSprite");

//         imgElement.src = pokemonSprite;
//         imgElement.style.display = "block";
//     }
//     catch(error){
//         console.error(error);
//     }
// }

fetchData();















