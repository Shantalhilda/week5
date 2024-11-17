function isPerfectNumber(num) {
    let sum = 0;
    for (let i = 1; i < num; i++) {
        if (num % i === 0) {
            sum += i;
        }
    }
    return sum === num;
}

console.log(isPerfectNumber(6)); // Output: true (6 = 1 + 2 + 3)
console.log(isPerfectNumber(28)); // Output: true (28 = 1 + 2 + 4 + 7 + 14)
