let myObject = {
  name: "Giorgi",
  age: 303333,
  city: "Somewhere",
  hobbies: ["reading", "coding"]
};

for (let key in myObject) {
  console.log(key + "  " + myObject[key]);
}