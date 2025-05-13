function sumArray(arr) {
    return arr.reduce((sum, num) => sum + num, 0);
}


function minMaxArray(arr) {
    return {
        min: Math.min(...arr),
        max: Math.max(...arr)
    };
}


function generateRandomArray(N) {
    return Array.from({ length: N }, () => Math.floor(Math.random() * 100) + 1);
}


function squareArray(arr) {
    return arr.map(num => num * num);
}



function roundNumber(num) {
    return {
        floor: Math.floor(num),
        ceil: Math.ceil(num),
        round: Math.round(num)
    };
}