function wordCount(str) {
    return str.trim().split(/\s+/).length;
}

console.log(wordCount("The quick brown fox jumps over the lazy dog")); // Output: 9
