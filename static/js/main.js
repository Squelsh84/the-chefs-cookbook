
// https://stackoverflow.com/questions/9173182/add-remove-input-field-dynamically-with-jquery

// Add Ingredients-Add recipe
var directionCount = $(".ingredient").length;
// add new cloned item 
$(".add-ingredient").on("click", function () {
  // clone and remove existing values 
  $(".new-ingredient:first").clone().insertBefore(".add-ingredient").find("input[type='text'], select, textarea").val("");
  // increase counter so original direction is never removed 
  directionCount += 1;
});
// delete last cloned item 
$(".remove-ingredient").on("click", function () {
  if (directionCount > 1) {
    // only remove the :last item 
    $(this).siblings(".new-ingredient:last").remove();
    // ensure original direction line never gets deleted 
    directionCount -= 1;
  }
});


// Add Method-Add recipe
var directionCount = $(".method").length;
// add new cloned item 
$(".add-method").on("click", function () {
  // clone and remove existing values 
  $(".new-method:first").clone().insertBefore(".add-method").find("input[type='text'], select, textarea").val("");
  // increase counter so original direction is never removed 
  directionCount += 1;
});
// delete last cloned item 
$(".remove-method").on("click", function () {
  if (directionCount > 1) {
    // only remove the :last item 
    $(this).siblings(".new-method:last").remove();
    // ensure original direction line never gets deleted 
    directionCount -= 1;
  }
});


// Print Function to print the page 

function myFunction() {
  window.print();
}



