let level = 1;
let attempts = [1, 1, 1, 1]; // Track attempts per level
let ranges = [3, 5, 10, 100]; // Level difficulty
let randomNums = [
    Math.floor(Math.random() * 4),   // Level 1: 0-3
    Math.floor(Math.random() * 6),   // Level 2: 0-5
    Math.floor(Math.random() * 11),  // Level 3: 0-10
    Math.floor(Math.random() * 101)  // Level 4: 0-100
];

function checkGuess() {
    let userInput = document.getElementById("user-input").value;
    let resultText = document.getElementById("result");

    if (userInput === "" || isNaN(userInput)) {
        resultText.innerText = "⚠️ Enter a valid number!";
        return;
    }

    let num = parseInt(userInput);

    if (num === randomNums[level - 1]) {
        resultText.innerText = `🎉 Correct! The number was ${num}. You guessed it in ${attempts[level - 1]} attempts!`;
        
        if (level < 4) {
            level++;
            nextLevel();
        } else {
            resultText.innerText += " 🎮 Game Over! You've beaten all levels!";
        }
    } else {
        attempts[level - 1]++;
        if (num < randomNums[level - 1]) {
            resultText.innerText = "❌ Too low! Try again.";
        } else {
            resultText.innerText = "❌ Too high! Try again.";
        }
    }
}

function nextLevel() {
    document.getElementById("level-text").innerText = `Level ${level}: Guess a number between 0 and ${ranges[level - 1]}`;
    document.getElementById("result").innerText = `🎯 New Level ${level}! Try guessing again.`;
}
