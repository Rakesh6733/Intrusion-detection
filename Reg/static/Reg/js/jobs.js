// Get the input field and assign it to a variable
var input = document.getElementById("search-input");

// Add a keyup event listener to the input field
input.addEventListener("keyup", function() {

  // Get the filter value entered by the user and convert it to uppercase
  var filter = input.value.toUpperCase();

  // Get all the job cards in the container and assign them to a variable
  var cards = document.querySelectorAll(".container .card");

  // Loop through all the job cards and hide those that do not match the search query
  for (var i = 0; i < cards.length; i++) {
    var title = cards[i].querySelector(".card-title .heading");
    var text = title.textContent || title.innerText;
    if (text.toUpperCase().indexOf(filter) > -1) {
      cards[i].style.display = "";
    } else {
      cards[i].style.display = "none";
    }
  }
});
