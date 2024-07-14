function likes(){
    document.querySelectorAll('.favorito-card').forEach(favorito => {
        favorito.addEventListener('click', () => {
            favorito.classList.toggle('liked');
        })
    });

    document.querySelectorAll('.boton-card').forEach(boton => {
        boton.addEventListener('click', () => {
            console.log(boton.id);
            const boton_id = boton.id.split('-')[1];
            const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            fetch(`/add_to_cart/${boton_id}`, {
                method: 'POST',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrftoken,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({})
            })
            .then(response => {
                if(!response.ok){
                    throw new Error('No se pudo cargar el archivo');
                }
                else return response.text();
            })
        })
    })
}

export { likes };