//  ES6გამოვიდა 2015 წლის ივნისში. 
//                           updates:
//  let და const:
let x = 10;
x = 20;         // შეიძლება შეცვლა
const y = 30;
// y = 40;      // const ცვლადის მნიშვნელობა ვერ შეიცვლება

// Arrow Functions:
const add = (a, b) => a + b;
console.log(add(2, 3)); 




const fruits = ["apple", "banana", "cucumber"];

for (const fruit of fruits) {
    console.log(fruit);
}


const person = {
    name: "Gio",
    age: 3000,
    city: "IDK"
};

for (const key in person) {
    console.log(`${key}: ${person[key]}`);
}


const target = { a: 1 };
const source1 = { b: 2 };
const source2 = { c: 3 };

const result = Object.assign(target, source1, source2);





const greet = () => "Hello, World!";
console.log(greet()); 