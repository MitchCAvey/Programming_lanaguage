

const cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K'];

/*
// Don't use this method, as it comes less efficient as the array gets bigger
cards,sort(() => Math.random() - 0.5);

console.log(cards);
*/

// Fisher-Yates algorithm

function shuffle(array){
    for(let i = array.length - 1; i > 0; i--){
        const random = Math.floor(Math.random() * (i + 1));

        [array[i], array[random]] = [array[random], array[i]];
    }
}

shuffle(cards);

console.log(cards);
