function calculateIncome(kilometers, isRushHour) {
    let incomePerKm = 2000;
    let bonusPerKm = isRushHour ? 500 : 0;
    return kilometers * (incomePerKm + bonusPerKm);
}

let kilometersTraveled = 50; // Kilometers traveled in a day
let isRushHour = true; // Indicate if the trip was during rush hour

let dailyIncome = calculateIncome(kilometersTraveled, isRushHour);
console.log(`The total income for the day is UGX ${dailyIncome}`);