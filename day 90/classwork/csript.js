class BankAccount {
    #balance;
    #pin;

    constructor(balance, pin) {
        this.#balance = balance;
        this.#pin = pin;
    }

    deposit(amount) { this.#balance += amount; }

    set pin(newPin) { this.#pin = newPin; }
}

const account = new BankAccount(500, "1234");
account.deposit(100);           
account.pin = "5678";         






class UserProfile {
    #username;
    #email;
    #password;

    constructor(username, email, password) {
        this.#username = username;
        this.#email = email; 
        this.#password = password;
    }

    #validatePassword(inputPassword) {
        return this.#password === inputPassword;
    }

    updateEmail(newEmail) {
        const atIndex = newEmail.indexOf('@');
        const dotIndex = newEmail.lastIndexOf('.');

        if (
            atIndex > 0 &&                      
            dotIndex > atIndex + 1 &&          
            !newEmail.includes(' ') &&           
            dotIndex < newEmail.length - 1       
        ) {
            this.#email = newEmail;
            return "Email updated successfully";
        }
        return "Invalid email format";
    }

    updatePassword(oldPassword, newPassword) {
        if (!this.#validatePassword(oldPassword)) {
            return "Incorrect current password";
        }
        if (newPassword.length < 8) {
            return "Password must be at least 8 characters";
        }
        this.#password = newPassword;
        return "Password updated successfully";
    }

    getUsername() {
        return this.#username;
    }
}










class Car {
    #engineStatus = false;
    #speed = 0;
    #fuelLevel;

    constructor(fuelLevel) {
        this.#fuelLevel = fuelLevel;
    }

    #startEngine() {
        if (this.#fuelLevel > 0) {
            this.#engineStatus = true;
            return "Engine started";
        }
        return "Not enough fuel";
    }

    #consumeFuel(amount) {
        this.#fuelLevel -= amount;
        if (this.#fuelLevel < 0) this.#fuelLevel = 0;
    }

    drive(speed) {
        if (!this.#engineStatus) return "Start the engine first";
        if (speed <= 0) return "Invalid speed";
        
        const fuelNeeded = speed * 0.1;
        if (fuelNeeded > this.#fuelLevel) return "Not enough fuel";
        
        this.#speed = speed;
        this.#consumeFuel(fuelNeeded);
        return `Driving at ${speed} km/h. Fuel remaining: ${this.#fuelLevel}L`;
    }

    refuel(amount) {
        if (amount <= 0) return "Invalid amount";
        this.#fuelLevel += amount;
        return `Refueled. Current fuel: ${this.#fuelLevel}L`;
    }

    stop() {
        this.#speed = 0;
        this.#engineStatus = false;
        return "Car stopped";
    }
}











class LibraryBook {
    #title;
    #author;
    #isCheckedOut = false;

    constructor(title, author) {
        this.#title = title;
        this.#author = author;
    }

    #toggleCheckOutStatus() {
        this.#isCheckedOut = !this.#isCheckedOut;
    }

    checkOut() {
        if (this.#isCheckedOut) return "Book already checked out";
        this.#toggleCheckOutStatus();
        return "Book checked out successfully";
    }

    returnBook() {
        if (!this.#isCheckedOut) return "Book already available";
        this.#toggleCheckOutStatus();
        return "Book returned successfully";
    }

    getBookInfo() {
        return `${this.#title} by ${this.#author}`;
    }
}









class SmartLight {
    #brightness = 50;
    #color = "white";
    #isOn = false;

    #validateBrightness(brightness) {
        return brightness >= 0 && brightness <= 100;
    }

    #validateColor(color) {
        const validColors = ["white", "red", "blue", "green", "yellow"];
        return validColors.includes(color.toLowerCase());
    }

    turnOn() {
        this.#isOn = true;
        return "Light turned on";
    }

    turnOff() {
        this.#isOn = false;
        return "Light turned off";
    }

    adjustBrightness(level) {
        if (!this.#validateBrightness(level)) return "Brightness must be between 0-100";
        this.#brightness = level;
        return `Brightness set to ${level}%`;
    }

    changeColor(color) {
        if (!this.#validateColor(color)) return "Invalid color";
        this.#color = color.toLowerCase();
        return `Color changed to ${this.#color}`;
    }
}






