function myFunction() {
     var input, filter, cards, cardContainer, h5, title, i;
     input = document.getElementById("myFilter");
     filter = input.value.toUpperCase();
     cardContainer = document.getElementById("myItems");
     cards = cardContainer.getElementsByClassName("card");
     for (i = 0; i < cards.length; i++) {
         title = cards[i].querySelector(".card-body h5.card-title");
         if (title.innerText.toUpperCase().indexOf(filter) > -1) {
             cards[i].style.display = "";
         } else {
             cards[i].style.display = "none";
         }
     }
 }

// $(document).ready(function(){
//     $("#myInput").on("keyup", function() {
//       var value = $(this).val().toLowerCase();
//       $("#myList li").filter(function() {
//         $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
//       });
//     });
//   });