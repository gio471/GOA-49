//  შეასრულეთ შემდეგი ქოუდვარსები JavaScript-ით:

//  8 kyu
//  https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/javascript:

function solution(str) {
    return str.split('').reverse().join('');
}

//  https://www.codewars.com/kata/5bb904724c47249b10000131/train/javascript:


function points(games) {
    let totalPoints = 0;
    for (const game of games) {
        const [x, y] = game.split(':').map(Number);
        if (x > y) {
            totalPoints += 3;
        } else if (x === y) {
            totalPoints += 1;
        }
    }
    return totalPoints;
}

//  7 kyu
//  https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/javascript:

const binaryArrayToNumber = arr => {
    const binaryString = arr.join('');
    return parseInt(binaryString, 2);
};

//  https://www.codewars.com/kata/57a049e253ba33ac5e000212/train/javascript:

function factorial(n) {
    let result = 1;
    for (let i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

//  https://www.codewars.com/kata/51f2b4448cadf20ed0000386/train/javascript:

function removeUrlAnchor(url) {
    return url.split('#')[0];
}


//  6 kyu
//  https://www.codewars.com/kata/57f8ff867a28db569e000c4a/train/javascript:

function kebabize(str) {
    let result = '';
    for (let i = 0; i < str.length; i++) {
        const char = str[i];
        if (char === char.toUpperCase() && char !== char.toLowerCase()) {
            if (i !== 0) {
                result += '-';
            }
            result += char.toLowerCase();
        } else if (isNaN(char) || char === ' ') {
            result += char.toLowerCase();
        }
        
    }
    return result;
}