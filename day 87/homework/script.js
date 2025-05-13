function sum(...numbers) {
    return numbers.reduce((total, num) => total + num, 0);
  }
  console.log(sum(1, 2, 3, 4)); 

  const [first, ...rest] = [1, 2, 3, 4, 5];
  console.log(first); 
  console.log(rest); 
  

  const person = { name: 'Giorgi', age: 12340, city: "New York" };
  const { name, ...details } = person;
  console.log(name); 
  console.log(details); 





const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const combined = [...arr1, ...arr2];
console.log(combined); 


const obj1 = { a: 1, b: 2 };
const obj2 = { c: 3, d: 4 };
const merged = { ...obj1, ...obj2 };
console.log(merged); 


const numbers = [1, 2, 3];
function add(a, b, c) {
  return a + b + c;
}
console.log(add(...numbers)); 




function processUser(firstName, lastName, ...hobbies) {
    const user = {
      name: `${firstName} ${lastName}`,
      hobbies: [...hobbies]
    };
    
    return user;
  }
  
  const user = processUser("Giorgi", "giviashili", "Reading","coding","styding");
  console.log(user);




//   localStorage საშუალებას გვაძლევს მონაცემების შენახვას ბრაუზერში კლიენტის მხარეს.


