function isPerfectSquare(num) {
    if (num < 1) return false;
    for (let i = 1; i * i <= num; i++) {
        if (i * i === num) return true;
    }
    return false;
}

console.log(isPerfectSquare(16)); // Output: true
console.log(isPerfectSquare(15)); // Output: false
