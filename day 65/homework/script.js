function func(name,age,color,country,city){
    this.name = name;
    this.age = age;
    this.color = color
    this.country = country
    this.city = city
}


function Motorcycle(brand, model, year, topSpeed) {
    this.brand = brand;
    this.model = model;
    this.year = year;
    this.topSpeed = topSpeed;

    this.accelerate = function() {
        console.log(`The ${this.brand} ${this.model} is accelerating to ${this.topSpeed} km/h!`);
    };
}