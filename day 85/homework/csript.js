const myArray = [10, 20, 30, 40, 50];
const [first, second, third, fourth, fifth] = myArray;

console.log(first); 
console.log(second); 
console.log(third);  
console.log(fourth); 
console.log(fifth);  





const person = {
    name: "Givi",
    age: 25,
    profession: "Developer"
};
const { name2, age, profession } = person;
  
console.log(name2);       
console.log(age);        
console.log(profession); 


/*
Rest collects elements into an array or object
Spread expands an array/object into elements
*/

function sum(...numbers) {
    return numbers.reduce((total, num) => total + num, 0);
}
  
console.log(sum(1, 2, 3));       
console.log(sum(10, 20));        
console.log(sum(5, 10, 15, 20)); 

const originalArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const copiedArray = [...originalArray];
  
console.log(copiedArray);
console.log(originalArray === copiedArray); 




const user = {
    id: 1,
    name: "Giorgi",
    email: 'nsjfhe@gmail.com',
    age: 123430,
    isAdmin: false
};
  

const { id, name1, ...rest } = user;
  
console.log(id);    
console.log(name1);  
console.log(rest);  