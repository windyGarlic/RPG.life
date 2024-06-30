document.addEventListener('DOMContentLoaded', async function() {
    showLoadingIndicator();
    try {
        const response = await fetch('http://127.0.0.1:5000/api/classes');
        const data = await response.json();
        console.log('Classes:', data);

        const mainElement = document.querySelector('.class-container');
        if (mainElement) {
            const classes = Array.isArray(data) ? data : [data];
//            mainElement.innerHTML = ''; // Clear existing content
            classes.forEach(cls => {
                const classElement = document.createElement('div');
                classElement.classList.add('class-item');
                classElement.innerHTML = `
                    <h3>${cls.name}</h3>
                    <p>${cls.description}</p>
                    <p>Experience: ${cls.experience_reward}</p>
                    <button class='delete-button' data-id='${cls.id}'>Delete Class</button>
                `;
                mainElement.appendChild(classElement);
            });

            document.querySelectorAll('.delete-button').forEach(button => {
                button.addEventListener('click', async function() {
                    const classId = this.getAttribute('data-id');
                    try {
                        const response = await fetch(`http://127.0.0.1:5000/api/classes/${classId}`, {
                            method: 'DELETE'
                        });
                        if (response.ok) {
                            alert('Class deleted successfully');
                            this.parentElement.remove(); 
                        } else {
                            alert('Failed to delete class');
                        }
                    } catch (error) {
                        console.error('Error:', error);
                        alert('Failed to delete class');
                    }
                });
            });
        }
    } catch (error) {
        handleCommonErrors(error);
    } finally {
        hideLoadingIndicator();
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById("class-form-modal");
    const btn = document.getElementById("new-class-btn");
    const span = document.getElementsByClassName("close-btn")[0];
    const form = document.getElementById("class-form");

    btn.onclick = function() {
        modal.style.display = "block";
    }

    span.onclick = function() {
        modal.style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    form.addEventListener('submit', async function(event) {
        event.preventDefault(); 
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        try {
            const response = await fetch('http://127.0.0.1:5000/api/classes', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            if (response.ok) {
                alert('Class created successfully!');
                modal.style.display = "none"; 
                form.reset(); 
                const mainElement = document.querySelector('main');
                if (mainElement) {
                    mainElement.innerHTML = ''; 
                }

                document.dispatchEvent(new Event('DOMContentLoaded'));
            } else {
                alert('Failed to create class');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Failed to create class');
        }
    });
});
