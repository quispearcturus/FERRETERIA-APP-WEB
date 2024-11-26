
function redirectUrl(id) {
    try {
        const linkElement = document.getElementById(id);
        // console.log(linkElement.tagName)

        if (!linkElement) {
            throw new Error(`El elemento con ID '${id}' no se encontró.`);
        }


        linkElement.addEventListener('click', function () {
            const url = this.getAttribute('data-url');
            if (!url) {
                throw new Error("El atributo 'data-url' no está definido.");
            }

            window.location.href = url;
        });



    } catch (error) {
        // console.error("Error:", error.message);
        // alert(error.message);
    }
}

function injectionButtonPassword() {
    const passwordInputs = document.querySelectorAll('.mx-password');

    passwordInputs.forEach(input => {
        // Crea el nuevo elemento HTML
        const newButton = document.createElement('button');
        newButton.type = "button"
        newButton.classList.add('toggle-password', 'mdl-button', 'mdl-js-button', 'mdl-button--icon');
        const newIcon = document.createElement('icon')
        newIcon.textContent = 'visibility'
        newIcon.classList.add('material-icons');

        newButton.appendChild(newIcon);
        const iid = input.id;

        //newButton.addEventListener('click', buttonPassword(iid, newIcon));
        newButton.addEventListener('click', () => {
            const passwordInput = document.getElementById(iid);
            const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
            passwordInput.setAttribute('type', type);
            newIcon.textContent = type === 'password' ? 'visibility' : 'visibility_off';
            passwordInput.focus();
        });
        input.insertAdjacentElement('afterend', newButton);
    });
}

// Llama a la función para inyectar mensajes
injectionButtonPassword();
Waves.init();
Waves.attach('.flat-buttons', ['waves-button']);
Waves.attach('.float-buttons', ['waves-button', 'waves-float']);
Waves.attach('.float-button-light', ['waves-button', 'waves-float', 'waves-light']);
Waves.attach('.float-box', ['waves-block', 'waves-float']);