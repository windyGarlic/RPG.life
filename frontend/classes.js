// script_classes.js or script_common.js

document.addEventListener('DOMContentLoaded', async function() {
    showLoadingIndicator();
    try {
        const classes = await fetchData('http://127.0.0.1:5000/api/classes/1');
        console.log('Classes:', classes);

        const mainElement = document.querySelector('main');
        if (mainElement) {

            classes.forEach(cls => {
                const classElement = document.createElement('div');
                classElement.classList.add('class-item');
                classElement.innerHTML = `
                    <h3>${cls.name}</h3>
                    <p>${cls.description}</p>
                    <p>Experience: ${cls.experience}</p>
                `;
                mainElement.appendChild(classElement);
            });
        }
    } catch (error) {
        handleCommonErrors(error);
    } finally {
        hideLoadingIndicator();
    }
});
