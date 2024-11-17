function getDayName(dateString) {
    const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    let date = new Date(dateString);
    return days[date.getDay()];
}

console.log(getDayName("2024-11-09")); // Output: "Saturday"
