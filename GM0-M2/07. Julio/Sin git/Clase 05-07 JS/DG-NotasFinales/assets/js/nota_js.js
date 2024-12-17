// Operación para carlcular la nota de JS

// Ingreso de nota 1 de JS
let nota_ingresada_js_1 = +prompt("Ingresa la nota 1 de JavaScript");
JAVASCRIPT1.innerHTML = nota_ingresada_js_1;

// Ingreso de nota 2 de JS
let nota_ingresada_js_2 = +prompt("Ingresa la nota 2 de JavaScript");
JAVASCRIPT2.innerHTML = nota_ingresada_js_2;

// Ingreso de nota 3 de JS
let nota_ingresada_js_3 = +prompt("Ingresa la nota 3 de JavaScript");
JAVASCRIPT3.innerHTML = nota_ingresada_js_3;

// Calcular promedio de nota JS
JAVASCRIPTPromedio.innerHTML = (
  (nota_ingresada_js_1 + nota_ingresada_js_2 + nota_ingresada_js_3) /
  3
).toFixed(2);
