// script_classes.js or script_common.js

document.addEventListener('DOMContentLoaded', async function() {
    showLoadingIndicator();
    try {
        const classes = await fetchData('http://127.0.0.1:5000/api/users/1/classes');
        console.log('Classes:', classes);

        const mainclassElement = document.querySelector('.class-container');
        if (mainclassElement) {

            classes.forEach(cls => {
                const classElement = document.createElement('div');
                classElement.classList.add('class-item');
                classElement.innerHTML = `
                    <h3>Class: ${cls.class_id}</h3>
                    <p>Experience: ${cls.experience_points}</p>
                    <p>ID: ${cls.id}</p>
                    <p>Level: ${cls.level}</p>

                `;
                mainclassElement.appendChild(classElement);

                
            });
            
        }

    } catch (error) {
        handleCommonErrors(error);
    } finally {
        hideLoadingIndicator();
    }
    try {
        const tasks = await fetchData('http://127.0.0.1:5000/api/users/1/tasks');
        console.log('Tasks:', tasks);

        const userQuest = document.querySelector('.user-quest-container');
        if (userQuest) {

            tasks.forEach(tsk => {
                const classElement = document.createElement('div');
                classElement.classList.add('user-quest');
                classElement.innerHTML = `
                    <h3>ID: ${tsk.id}</h3>
                    <p>Status: ${tsk.status}</p>
                    <p>Date Started: ${tsk.date_started}</p>
                    <p>Level: ${tsk.date_completed}</p>

                `;
                userQuest.appendChild(classElement);

                
            });
            
        }

    } catch (error) {
        handleCommonErrors(error);
    } finally {
        hideLoadingIndicator();
    }
});
