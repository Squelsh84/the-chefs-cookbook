// Add Ingredients-Add recipe
var directionCount = $(".ingredient").length;
/* add new cloned item */
$(".add-ingredient").on("click", function () {
  /* clone and remove existing values */
  $(".new-ingredient:first").clone().insertBefore(".add-ingredient").find("input[type='text'], select, input").val("");
  /* increase counter so original direction is never removed */
  directionCount += 1;
});
/* delete last cloned item */
$(".remove-ingredient").on("click", function () {
  if (directionCount > 1) {
    /* only remove the :last item */
    $(this).siblings(".new-ingredient:last").remove();
    /* ensure original direction line never gets deleted */
    directionCount -= 1;
  }
});