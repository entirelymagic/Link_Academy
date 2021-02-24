// We get the paragraph with a specific id and asociate it with a variable.
var redplanet = document.getElementById('redplanet');

// A better way to select an element is using querySelector
var blueplanet = document.querySelector('#blueplanet');



//blueplanet.remove() // will remove the planet 

function press_me() {
    // A fucntion that will change the elements selected
    redplanet.innerHTML = "<h1>Welcome to Mars!</h1>"
    redplanet.classList.add("alert", "alert-danger")
    blueplanet.innerText = "Thank you for keeping me clean!"
}

// Select the button
var button = document.querySelector("input[type='button']")

//add an event listener ( type of event) and what to do when it happens
button.addEventListener("click" , press_me)

