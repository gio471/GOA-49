console.log(5 == 5);  
console.log(5 == '5');
console.log(5 == 6);
console.log('hello' == 'hello');
console.log(0 == false);


console.log(5 === 5);  
console.log(5 === '5');  
console.log(0 === false);
console.log(true === true); 
console.log('5' === 5);


console.log(5 != 4);  
console.log(5 != 5);  
console.log('hello' != 'world'); 
console.log(true != false);  
console.log(5 != '5'); 


console.log(5 !== 4);  
console.log(5 !== '5'); 
console.log(5 !== 5);
console.log('true' !== true); 
console.log(0 !== false);  


console.log(5 < 10);  
console.log(5 < 3);  
console.log(3 < 3);  
console.log('a' < 'b');  
console.log(10 < 5);  


// alert ფუნქცია გამოსახავს შეტყობინებას მომხმარებლისთვის, რომელშიც მას შეუძლია მხოლოდ "OK" ღილაკზე დაჭერა.
// confirm სთავაზობს მომხმარებელს ორ შესაძლებლობას: "OK" ან "Cancel". ეს ფუნქცია აბრუნებს true თუ მომხმარებელმა დააჭირა "OK", და false თუ "Cancel".
// prompt ნაჩვენებია როგორც ტექსტური ველი, სადაც მომხმარებელი უნდა შეიყვანოს გარკვეული მნიშვნელობა. ის აბრუნებს შეყვანილ მნიშვნელობას ან null, თუ მომხმარებელმა დააჭირა "Cancel".

const response = confirm("are you adult?: ");

if (response){
    console.log("you are adult.");
} else{
    console.log("you aren't adult.")
}
