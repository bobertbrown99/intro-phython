// Get the current date
const currentDate = new Date();

// Get the month and day of the current date
const currentMonth = currentDate.getMonth() + 1; // Months are zero-based, so we add 1
const currentDay = currentDate.getDate();

// Check if it's Christmas
if (currentMonth === 12 && currentDay === 25) {
    console.log("It's Christmas!");
} else {
    console.log("It's not Christmas yet.");
}
