class Thermostat {
    #temperature;
    #minTemp;
    #maxTemp;
    #mode;

    constructor(minTemp, maxTemp, initialTemp, mode) {
    this.#minTemp = minTemp;
    this.#maxTemp = maxTemp;
    this.#temperature = this.#clampTemperature(initialTemp);
    this.#mode = mode;
    }

    #clampTemperature(value) {
    return Math.max(this.#minTemp, Math.min(this.#maxTemp, value));
    }

    #setTemperature(value) {
    this.#temperature = this.#clampTemperature(value);
    }

    adjustTemperature(value) {
    this.#setTemperature(value);
    }

    changeMode(mode) {
    this.#mode = mode;
    }

    getCurrentTemperature() {
    return this.#temperature;
    }
}




class SecureNote {
    #content;
    #pin;

    constructor(content, pin) {
    this.#content = content;
    this.#pin = pin;
    }

    #validatePin(pin) {
    return this.#pin === pin;
    }

    updateContent(newContent, pin) {
    if (this.#validatePin(pin)) {
        this.#content = newContent;
        return true;
    }
    return false;
    }

    getContent(pin) {
    if (this.#validatePin(pin)) {
        return this.#content;
    }
    return "Invalid PIN";
    }
}



class InventoryItem {
    #name;
    #quantity;
    #cost;

    constructor(name, quantity, cost) {
    this.#name = name;
    this.#quantity = quantity;
    this.#cost = cost;
    }

    #validateQuantityChange(amount) {
    return this.#quantity + amount >= 0;
    }

    restock(amount) {
    if (amount > 0) {
        this.#quantity += amount;
        return true;
    }
    return false;
    }

    sell(amount) {
    if (this.#validateQuantityChange(-amount)) {
        this.#quantity -= amount;
        return true;
    }
    return false;
    }

    getInfo() {
    return {
        name: this.#name,
        quantity: this.#quantity,
        cost: this.#cost
    };
    }
}




class EmailClient {
    #email;
    #password;
    #inbox;
    constructor(email, password) {
    this.#email = email;
    this.#password = this.#hashPassword(password);
    this.#inbox = [];
    }

    #hashPassword(password) {
    return password.split('').reverse().join('');
    }

    #validatePassword(password) {
    return this.#password === this.#hashPassword(password);
    }

    #receiveEmail(email) {
    this.#inbox.push(email);
    }

    login(password) {
    return this.#validatePassword(password);
    }

    sendEmail(to, message) {
    console.log(`Email sent to ${to}: ${message}`);
    return true;
    }

    readInbox() {
    return [...this.#inbox];
    }
}





class Subscription {
    #userID;
    #plan;
    #paymentMethod;
    constructor(userID, plan, paymentMethod) {
    this.#userID = userID;
    this.#plan = plan;
    this.#paymentMethod = paymentMethod;
    }
    #validatePayment(paymentMethod) {
    return typeof paymentMethod === 'string' && paymentMethod.length > 0;
    }

    upgradePlan(newPlan) {
    if (this.#validatePayment(this.#paymentMethod)) {
        this.#plan = newPlan;
        return true;
    }
    return false;
    }
    changePaymentMethod(newMethod) {
    if (this.#validatePayment(newMethod)) {
        this.#paymentMethod = newMethod;
        return true;
    }
    return false;
    }

    getSubscriptionInfo() {
    return {
        userID: this.#userID,
        plan: this.#plan
    };
    }
}



