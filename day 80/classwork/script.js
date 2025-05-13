//  8 kyu
//  https://www.codewars.com/kata/53dc54212259ed3d4f00071c:

function sum (numbers) {
    let total = 0;
    for (let num of numbers){
      total += num;
    }
    return total
  }

//  https://www.codewars.com/kata/57a2013acf1fa5bfc4000921:

function findAverage(array) {
    if (array.length === 0) {
        return 0;
    }
    let sum = 0;
    for (let num of array) {
        sum += num;
    }
    return sum / array.length;
}

//  https://www.codewars.com/kata/5513795bd3fafb56c200049e:

function countBy(x, n) {
    let result = [];
    for (let i = 1; i <= n; i++) {
        result.push(x * i);
    }
    return result;
}

//  https://www.codewars.com/kata/5a00e05cc374cb34d100000d:

const reverseSeq = n => {
    let result = [];
    for (let i = n; i >= 1; i--) {
        result.push(i);
    }
    return result;
};


//  6 kyu
//  https://www.codewars.com/kata/5839edaa6754d6fec10000a2:

function findMissingLetter(array) {
    const alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    
    for(let i = 0; i < array.length - 1; i++) {
      if(alphabet[alphabet.indexOf(array[i]) + 1] !== array[i + 1]) {
        return alphabet[alphabet.indexOf(array[i]) + 1];
      }
    }
    
  }