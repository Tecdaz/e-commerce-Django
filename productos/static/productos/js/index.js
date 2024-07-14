const iconoBolsa = document.querySelector('.icono-bolsa');
iconoBolsa.addEventListener('click', () => {
    const carrito = document.querySelector(".carrito");
    carrito.classList.toggle("mostrar-carrito");
    iconoBolsa.classList.toggle('rotate');
    if(iconoBolsa.classList.contains('rotate')){
        iconoBolsa.classList.remove("bi-bag");
        iconoBolsa.classList.add("bi-bag-x");
    }else{
        iconoBolsa.classList.remove("bi-bag-x");
        iconoBolsa.classList.add("bi-bag");
    }
});

const iconoMenu = document.querySelector('.list-icon');
iconoMenu.addEventListener('click', () => {
    const body = document.querySelector('body');
    const subMenu = document.querySelector('.contenedor-menu-mobile');
    subMenu.classList.toggle('mostrar-contenedor-menu');
    iconoMenu.classList.toggle('girar');
    body.classList.toggle('no-scroll');
    if(iconoMenu.classList.contains('girar')){
        iconoMenu.classList.remove("bi-list");
        iconoMenu.classList.add("bi-x-lg");

    }else{
        iconoMenu.classList.remove("bi-x-lg");
        iconoMenu.classList.add("bi-list");
    }
});