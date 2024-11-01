function getCallRate(networkCode) {
    let callRate;

    switch (networkCode) {
        case 1:
            callRate = "MTN: 5 cents per minute";
            break;
        case 2:
            callRate = "Airtel: 6 cents per minute";
            break;
        case 3:
            callRate = "Africell: 4 cents per minute";
            break;
        default:
            callRate = "Unknown network code";
    }

    console.log(callRate);
}
getCallRate();