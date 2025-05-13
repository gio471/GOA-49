let seconds = 0;
let minutes = 0;

function updateTimer() {
    seconds++;
    if (seconds >= 60) {
        seconds = 0;
        minutes++;
    }
    console.log(`Minutes: ${minutes}, Seconds: ${seconds}`);
}

setInterval(updateTimer, 1000);




let count = 0;

const interval = setInterval(() => {
    console.log(count);
    count++;
    if (count > 15) {
        clearInterval(interval);
    }
}, 500);



setTimeout(() => {
    console.log(2);
}, 1000);

setTimeout(() => {
    console.log(1);
}, 2000);

setTimeout(() => {
    console.log(3);
}, 3000);



