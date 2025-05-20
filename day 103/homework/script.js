const immediatePromise = new Promise((resolve) => {
    resolve("Hello, Promise!");
});

immediatePromise.then(message => console.log(message));


const errorPromise = new Promise((resolve, reject) => {
    reject("Something went wrong!");
});

errorPromise
    .catch(error => console.error(error));



const delayedPromise = new Promise((resolve) => {
    setTimeout(() => {
    resolve("2 seconds have passed");
    }, 2000);
});

delayedPromise.then(message => console.log(message));




const numberPromise = new Promise((resolve) => {
    resolve(5);
});

numberPromise
.then(num => {
    console.log(num); 
    return num * 2;
})
.then(num => {
    console.log(num); 
    return num * 2;
})
.then(num => {
    console.log(num); 
    return num * 2;
});





