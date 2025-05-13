function calculateSum(...numbers) {
    return numbers.reduce((sum, num) => sum + num, 0);
}


console.log(calculateSum(1, 2, 3));         






const human = {
    name: "GIVIKOBABUA",
    age: 7974677
};

const army = {
    position: "General",
    Army: "USSR"
};

const employee = {
    ...human,
    ...army
};

console.log(human);









function sumArray(numbersArray) {
    return numbersArray.reduce((sum, num) => sum + num, 0);
}


console.log(sumArray([1, 2, 3, 4, 5]));       
console.log(sumArray([10, 20, 30]));          
console.log(sumArray([100]));                 
console.log(sumArray([]));                   








const fruits = ["apple","pineapple"];
const vegetables = ["potateo", "melon"];
const combinedArray = [...fruits, ...vegetables];

console.log(combinedArray); 
const moreFruits = ["watermelon", ...fruits, "orange"];
console.log(moreFruits);
