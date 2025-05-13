class Car {
    // Public class fields (no need to declare in constructor)
    make;
    model;
    
    constructor(make, model) {
        this.make = make;
        this.model = model;
    }
}




class BankAccount {
    #balance; 
    
    constructor(initialBalance = 0) {
        this.#balance = initialBalance;
    }
    
    deposit(amount) {
        if (amount > 0) {
            this.#balance += amount;
            return `Deposited $${amount}. New balance: $${this.#balance}`;
        }
        return "Deposit amount must be positive";
    }
    
    withdraw(amount) {
        if (amount > 0 && amount <= this.#balance) {
            this.#balance -= amount;
            return `Withdrew $${amount}. New balance: $${this.#balance}`;
        }
        return amount <= 0 ? "Withdrawal amount must be positive" : "Insufficient funds";
    }
    
    getBalance() {
        return this.#balance;
    }
}

const account = new BankAccount(100);
console.log(account.deposit(50)); 
console.log(account.withdraw(30));








class MathOperations {
    static PI = 3.141592653589793;
    
    static add(a, b) {
        return a + b;
    }
    
    static subtract(a, b) {
        return a - b;
    }
}

console.log(MathOperations.add(5, 3)); 
console.log(MathOperations.PI); 










class Rectangle {
    #width;
    #height;
    
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }
    
    get area() {
        return this.#width * this.#height;
    }
    
    set width(value) {
        if (value > 0) {
            this.#width = value;
        } else {
            console.error("Width must be positive");
        }
    }
    
    set height(value) {
        if (value > 0) {
            this.#height = value;
        } else {
            console.error("Height must be positive");
        }
    }
    
    get width() { return this.#width; }
    get height() { return this.#height; }
}

const rect = new Rectangle(10, 5);
console.log(rect.area); // 50
rect.width = -5; 














class User {
    #username;
    #password;
    
    constructor(username, password) {
        this.#username = username;
        this.setPassword(password);
    }
    
    #validatePassword(password) {
        return password.length >= 8 && 
                /[A-Z]/.test(password) && 
                /[0-9]/.test(password);
    }
    
    setPassword(newPassword) {
        if (this.#validatePassword(newPassword)) {
            this.#password = newPassword;
            return "Password updated successfully";
        }
        return "Password must be at least 8 characters with a number and uppercase letter";
    }
}

const user = new User("john_doe", "Weakpass"); 
const user2 = new User("jane_doe", "StrongPass1"); 













class Book {
    title;
    #pages;
    
    constructor(title, pages) {
        this.title = title;
        this.pages = pages;
    }
    
    get pages() {
        return this.#pages;
    }
    
    set pages(value) {
        if (value > 0) {
            this.#pages = value;
        } else {
            console.error("Page count must be positive");
        }
    }
}

const book = new Book("JavaScript Guide", 300);
console.log(book.title); 
console.log(book.pages); 
book.pages = -100; 













class Player {
    static #count = 0;
    name;
    
    constructor(name) {
        this.name = name;
        Player.#count++;
    }
    
    static getPlayerCount() {
        return Player.#count;
    }
}

const p1 = new Player("Alice");
const p2 = new Player("Bob");
console.log(Player.getPlayerCount()); 











class Vehicle {
    #speed = 0;
    
    accelerate(amount) {
        this.#speed += amount;
    }
    
    brake(amount) {
        this.#speed = Math.max(0, this.#speed - amount);
    }
    
    get speed() {
        return this.#speed;
    }
}

class Bike extends Vehicle {
    pedal(force) {
        this.accelerate(force * 0.5);
    }
}

const bike = new Bike();
bike.pedal(10);
console.log(bike.speed); 














class Student {
    constructor(name, grade) {
        this.name = name;
        this.grade = grade;
    }
    
    static compareGrades(student1, student2) {
        if (student1.grade > student2.grade) return `${student1.name} has higher grade`;
        if (student1.grade < student2.grade) return `${student2.name} has higher grade`;
        return "Both students have the same grade";
    }
}

const alice = new Student("Alice", 90);
const bob = new Student("Bob", 85);
console.log(Student.compareGrades(alice, bob)); 