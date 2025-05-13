const users = [
    { name: "Alice", age: 17 },
    { name: "Bob", age: 20 },
    { name: "Charlie", age: 25 }
];

const adultUsers = users.map(user => ({
    ...user,
    isAdult: user.age >= 18
}));

console.log(adultUsers);



const numbers = [30, 60, 80, 100, 120];

const result = numbers
.filter(num => num > 50)
.map(num => num / 2);

console.log(result); 





const words = ["apple", "banana", "apple", "orange", "banana", "apple"];

const wordFrequency = {};
words.forEach(word => {
wordFrequency[word] = (wordFrequency[word] || 0) + 1;
});

console.log(wordFrequency); 




const cars = [
    { brand: { name: "Toyota" }, model: "Corolla" },
    { brand: { name: "Honda" }, model: "Civic" },
    { brand: { name: "Toyota" }, model: "Camry" }
];

const toyotaCars = cars.filter(car => car.brand.name === "Toyota");
console.log(toyotaCars);
