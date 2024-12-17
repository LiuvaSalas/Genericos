/Inicializacion tooltip/;
const tooltipTriggerList = document.querySelectorAll(
  '[data-bs-toggle="tooltip"]'
);
const tooltipList = [...tooltipTriggerList].map(
  (tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl)
);

/Alertas de los botones/;
$("#enviar-correo").on("click", function () {
  alert("Correo Enviado...");
});

$("#favoritos").on("click", function () {
  alert("Añadido a favoritos...");
});

/Cambiar color a rojo/;
$("#ingredientes").on("dblclick", function () {
  $(this).css({
    color: "red",
  });
});

$("#preparacion").on("dblclick", function () {
  $(this).css({
    color: "red",
  });
});

/Esconder contenido de las cards/;
$("#recetas-relacionadas").on("click", function () {
  $("#recetas-relacionadas p").toggle("slow", function () {
    // Animation complete.
  });
});
