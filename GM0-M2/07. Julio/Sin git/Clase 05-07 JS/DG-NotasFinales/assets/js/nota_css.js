// Operación para carlcular la nota de CSS

// Ingreso de nota 1 de css
let nota_ingresada_css_1 = +prompt("Ingresa la nota 1 de CSS");
CSS1.innerHTML = nota_ingresada_css_1;

// Ingreso de nota 2 de css
let nota_ingresada_css_2 = +prompt("Ingresa la nota 2 de CSS");
CSS2.innerHTML = nota_ingresada_css_2;

// Ingreso de nota 3 de css
let nota_ingresada_css_3 = +prompt("Ingresa la nota 3 de CSS");
CSS3.innerHTML = nota_ingresada_css_3;

// Calcular promedio de nota CSS
CSSPromedio.innerHTML = (
  (nota_ingresada_css_1 + nota_ingresada_css_2 + nota_ingresada_css_3) /
  3
).toFixed(2);
