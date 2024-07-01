const swap = document.getElementById("elements");

new Sortable(swap,{
  animation: 360,
  chosenClass: "boxShadow",
  dragClass: "drag"
});
