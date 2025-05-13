// მსგავსებები:ორივე იყენებს key ვორდებს.ორივე საშუალებას გაძლევთ წვდომა მონაცემებზე key-ის საშუალებით.
// განსხავებები:სინტაქსი


let person = {
    name: "გიორგი",
    age: 13,
    greet: function() {
        console.log("Hello, my name is " + this.name);
    }
};

person.greet();


// ფუნქცია არის დამოუკიდებელი კოდის ბლოკი, რომელიც შეიძლება გამოიძახოს სახელით და შეიძლება მიიღოს არგუმენტები.
// მეთოდი არის ფუნქცია, რომელიც ასოცირებულია კონკრეტულ ობიექტთან ან კლასთან.
// მეთოდები გამოიძახება ობიექტის კონტექსტში და შეიძლება წვდომა ჰქონდეს ობიექტის მონაცემებს this-ის საშუალებით.


function Person(name, age, job) {
    this.name = name;
    this.age = age;
    this.job = job;
}

let person1 = new Person("Giorgi", 13, "Student");
console.log(person1); 




function Car(make, model, year, color, horsePower) {
    this.make = make;
    this.model = model;
    this.year = year;
    this.color = color;
    this.horsePower = horsePower;

    this.increaseHorsePower = function() {
        this.horsePower += 100;
        console.log(`New horse power: ${this.horsePower}`);
    };
}


