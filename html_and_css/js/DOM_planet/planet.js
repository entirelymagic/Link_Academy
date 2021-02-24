// We get the paragraph with a specific id and asociate it with a variable.
var redplanet = document.getElementById('redplanet');
var blueplanet = document.getElementById('blueplanet');

redplanet.innerHTML = "<h1>Welcome to Mars!</h1>"
redplanet.classList.add("alert", "alert-danger")


blueplanet.innerText = "Thank you for keeping me clean!"