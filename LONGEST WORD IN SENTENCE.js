function longestWord(sentence) {
    let words = sentence.split(' ');
    let longest = words.reduce((max, word) => word.length > max.length ? word : max, '');
    return longest;
}

console.log(longestWord("The quick brown fox jumped over the lazy dog")); // Output: "jumped"
