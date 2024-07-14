function likes(){
    document.querySelectorAll('.favorito-card').forEach(favorito => {
        favorito.addEventListener('click', () => {
            favorito.classList.toggle('liked');
        })
    });
}

export { likes };