// Authorized users and correct answers
const authorizedUsers = ["Henri", "Ernst", "Casper", "Monica", "Cappe", "Pavel"];
const correctAnswers = ["Asilo", "Asilo Argo", "Argo"];

function checkAuthorization() {
    const name = document.getElementById("name").value.trim(); // Get the name and trim any extra whitespace
    if (authorizedUsers.includes(name)) {
        // Hide the first question and show the second question
        document.getElementById("firstQuestion").style.display = "none";
        document.getElementById("questionSection").style.display = "block";
    } else {
        alert("Sorry, you are not authorized to play this game.");
    }
}

function checkAnswer() {
    const answer = document.getElementById("investment").value.trim(); // Get the answer and trim whitespace
    const overlay = document.getElementById("overlay");
    const overlayImage = document.getElementById("overlayImage");

    if (correctAnswers.includes(answer)) {
        // Display winner meme in overlay and play victory music
        overlayImage.src = "Game files/Winner_meme.jpeg"; // Path to the winner meme
        overlay.style.display = "flex"; // Show the overlay
        const victorySound = new Audio("Game files/Winner_song.mp3"); // Path to victory music
        victorySound.play();
    } else {
        // Display loser meme in overlay and play loser music
        overlayImage.src = "Game files/Loser_meme.png"; // Path to the loser meme
        overlay.style.display = "flex"; // Show the overlay
        const loserSound = new Audio("Game files/Loser_song.wav"); // Path to loser music
        loserSound.play();
    }
}

// Close the overlay when clicking anywhere on it
document.getElementById("overlay").addEventListener("click", function() {
    this.style.display = "none";
});

console.log("JavaScript is connected");
