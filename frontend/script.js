// script.js

// Function to fetch data from the API
function fetchData(url) {
    return fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .catch(error => {
            console.error('Error fetching data:', error);
            throw error; // Propagate the error for handling in the caller
        });
}

// Function to make a POST request to the API
function postData(url, data) {
    return fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .catch(error => {
        console.error('Error posting data:', error);
        throw error; // Propagate the error for handling in the caller
    });
}

// Function to display error messages on the page
function displayErrorMessage(message) {
    const errorElement = document.createElement('div');
    errorElement.classList.add('error-message');
    errorElement.textContent = message;
    document.body.appendChild(errorElement);
}

// Function to show loading indicator (placeholder implementation)
function showLoadingIndicator() {
    // Implement your loading indicator logic here (e.g., show a spinner or message)
    // For example:
    const loadingElement = document.createElement('div');
    loadingElement.classList.add('loading-indicator');
    loadingElement.textContent = 'Loading...';
    document.body.appendChild(loadingElement);
}

// Function to hide loading indicator (placeholder implementation)
function hideLoadingIndicator() {
    // Implement logic to hide loading indicator (e.g., remove spinner or hide message)
    // For example:
    const loadingElement = document.querySelector('.loading-indicator');
    if (loadingElement) {
        loadingElement.remove();
    }
}

// Function to handle common errors (e.g., network issues)
function handleCommonErrors(error) {
    console.error('Common error handler:', error);
    // Optionally, display a generic error message or handle specific error cases
}
