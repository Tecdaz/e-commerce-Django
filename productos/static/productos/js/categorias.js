import { likes } from "./likes.js";

document.addEventListener('DOMContentLoaded', () => {
    let categorias = document.querySelectorAll('.categoria');
    categorias.forEach(categoria => {
        categoria.addEventListener('click', () => {
            categorias.forEach(categoria => {
                categoria.classList.toggle('selected', false);
            });
            categoria.classList.toggle('selected', true);
            let nombre = categoria.getElementsByTagName('h2')[0].textContent;
            console.log(nombre);
            fetch(`/productos/${nombre}`)
            .then(response => {
                if(!response.ok){
                    throw new Error('No se pudo cargar el archivo');
                }
                else return response.text();
            })
            .then(html => {
                let contenedorProductos = document.querySelector(".contenedor-fetch");
                contenedorProductos.innerHTML="";
                contenedorProductos.innerHTML = html;
                likes();
            })
    })})
})