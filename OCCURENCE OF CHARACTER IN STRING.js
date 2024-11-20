function countOccurrences(str, char) {
    return str.split(char).length - 1;
}

console.log(countOccurrences("hello world", "o")); // Output: 2
console.log(countOccurrences("hello world", "l")); // Output: 3
