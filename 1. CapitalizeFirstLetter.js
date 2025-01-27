function capitalizeWords(string) {
    return stribg.split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
}

console.log(capitalizeWords("hello uganda")); // Output: "Hello uganda"
