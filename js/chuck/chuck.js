function showFact(joke) {
    document.querySelector("#fact").innerText = joke
}
// Call the API with get
axios.get("http://api.icndb.com/jokes/random?firstName=Elvis&lastName=")
    .then(response => showFact(response.data.value.joke))