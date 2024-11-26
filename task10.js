function fetchData(callback) {
    console.log("Fetching data from the server...");

    // Simulate a delay for fetching data using setTimeout
    setTimeout(function() {
        // Simulate data retrieval
        var data = { message: "Data successfully retrieved from the server." };

        // Call the callback function with the retrieved data
        callback(data);
    }, 2000); // 2-second delay to simulate server response time
}

// Callback function to display the message
function displayMessage(data) {
    console.log(data.message);
}


fetchData(displayMessage);

