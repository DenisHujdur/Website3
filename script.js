document.getElementById("printButton").addEventListener("click", function() {
  // Get the user input value
  var userInput = document.getElementById("userInput").value;

  // Send the user input to the backend API
  fetch('/ask_gpt', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ user_input: userInput })
  })
  .then(response => response.json())
  .then(data => {
    // Display the response from the backend (output from ChatGPT)
    document.getElementById("output").innerText = data.gpt_response;
  })
  .catch(error => {
    console.error('Error:', error);
  });
});