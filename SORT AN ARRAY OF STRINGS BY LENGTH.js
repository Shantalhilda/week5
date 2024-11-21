function sortByLength(arr) {
    return arr.sort((a, b) => a.length - b.length);
}

let words = ["apple", "banana", "pear", "kiwi"];
console.log(sortByLength(words)); // Output: ["kiwi", "pear", "apple", "banana"]
