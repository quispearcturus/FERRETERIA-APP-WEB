document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');

    if (form) {
        const inputs = form.querySelectorAll('input, select, textarea');
        console.log('start')
        inputs.forEach(input => {
            input.addEventListener('change', function() {
                setTimeout(() => {
                    form.submit(); // Enviar el formulario
                }, 500); // Retraso de 500 ms para evitar múltiples envíos
            });
        });
    }
});
