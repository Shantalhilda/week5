function containsSubstring(str, substring) {
    return str.indexOf(substring) !== -1;
}

console.log(containsSubstring("hello world", "world")); // Output: true
console.log(containsSubstring("hello world", "bye")); // Output: false
