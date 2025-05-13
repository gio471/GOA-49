let myList = new Array(5);

myList[0] = "Element 1";
myList[1] = "Element 2";
myList[2] = "Element 3";
myList[3] = "Element 4";
myList[4] = "Element 5";

for (let i = 0; i < myList.length; i++) {
    console.log(myList[i]);
}



let myList = new Array(4);

//  როდესაც new Array(4) გამოიყენება, ის ქმნის მასივს 4 ცარიელი ელემენტით.ეს ნიშნავს, რომ მასივის length იქნება 4, მაგრამ ყველა ელემენტი იქნება undefined.

console.log(myList); 



let myList = ["Element 1", "Element 2", "Element 3"];
console.log(myList); 




let myArray = [];
myArray["name"] = "Giorgi";
myArray["surname"] = "Alavidze";
myArray["age"] = 13;

console.log(myArray["name"]); 
console.log(myArray["surname"]); 
console.log(myArray["age"]);


console.log(myArray.length); 

// მასივის ზომა არის 0, რადგან JavaScript-ში მასივის length თვისება ითვლის მხოლოდ იმ ელემენტებს,
// რომლებიც არიან დანომრილი ინდექსებით (0, 1, 2, ...). როდესაც ჩვენ ვიყენებთ სტრიქონულ ინდექსებს
// (როგორიცაა "name", "surname", "age"), ეს ელემენტები არ ჩაითვლება მასივის length-ში.
// ამიტომ, მასივის ზომა რჩება 0, მიუხედავად იმისა, რომ ჩვენ დავამატეთ ელემენტები.
