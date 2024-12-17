// Operación para carlcular la nota de HTML

// Ingreso de nota 1 de html
let nota_ingresada_html_1 = +prompt("Ingresa la nota 1 de HTML");
HTML1.innerHTML = nota_ingresada_html_1;

// Ingreso de nota 2 de html
let nota_ingresada_html_2 = +prompt("Ingresa la nota 2 de HTML");
HTML2.innerHTML = nota_ingresada_html_2;

// Ingreso de nota 3 de html
let nota_ingresada_html_3 = +prompt("Ingresa la nota 3 de HTML");
HTML3.innerHTML = nota_ingresada_html_3;

// Calcular promedio de nota HTML
HTMLPromedio.innerHTML = (
  (nota_ingresada_html_1 + nota_ingresada_html_2 + nota_ingresada_html_3) /
  3
).toFixed(2);
