function hasUniqueChars(str) {
    let charSet = new Set();
    for (let char of str) {
        if (charSet.has(char)) {
            return false;
        }
        charSet.add(char);
    }
    return true;
}

console.log(hasUniqueChars("abcdef")); // Output: true
console.log(hasUniqueChars("hello")); // Output: false
