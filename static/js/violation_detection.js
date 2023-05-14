// JavaScript code in violation_detection.js

// Function to handle the form submission
function processVideo(event) {
    event.preventDefault();

    // Get the selected video file from the form
    const videoFile = document.getElementById('video-file').files[0];
    
    // Create a FormData object and append the video file
    const formData = new FormData();
    formData.append('video', videoFile);

    // Send a POST request to the Flask route
    fetch('/violation-detection', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Process the results received from the server
        displayResults(data.results);
    })
    .catch(error => {
        console.log('Error:', error);
    });
}

// Function to display the processed results
function displayResults(results) {
    const outputDiv = document.getElementById('output');

    // Clear the previous results
    outputDiv.innerHTML = '';

    // Iterate over the results and display them on the page
    results.forEach(result => {
        // Create an element to display the result
        const resultElement = document.createElement('p');
        resultElement.textContent = result;

        // Append the result element to the output div
        outputDiv.appendChild(resultElement);
    });
}

// Add an event listener to the form
const form = document.getElementById('video-form');
form.addEventListener('submit', processVideo);
