const users = [
    { id: 1, name: "Aniko" },
    { id: 2, name: "Byrt" },
    { id: 3, name: "gfh" }
];

const names = users.map(user => user.name);
console.log(names);





const products = [
    { name: "Laptop", price: 1000 },
    { name: "Mouse", price: 20 },
    { name: "Keyboard", price: 50 }
];

const cheapProducts = products.filter(product => product.price < 100);
console.log(cheapProducts); 



const books = [
    { title: "1384", author: "someone gg " },
    { title: "GOA CHAD", author: "sdmvhhk" }
];

const bookStrings = books.map(book => `${book.title} by ${book.author}`);
console.log(bookStrings); 





const numbers = [3, 9, 12, 15, 18, 20, 21];

const filteredNumbers = numbers.filter(num => num > 10 && num % 3 === 0);
console.log(filteredNumbers); 