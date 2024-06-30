document.addEventListener('DOMContentLoaded', async function() {
    showLoadingIndicator();
    try {
        const quests = await fetchData('http://127.0.0.1:5000/api/quests');
        console.log('quests:', quests);
        const questBoardElement = document.querySelector('.quest-board');
        if (questBoardElement) {
            questBoardElement.innerHTML = ''; // Clear existing content
            quests.forEach(quest => {
                const questElement = document.createElement('div');
                questElement.classList.add('quest-item');
                questElement.innerHTML = `
                    <b>${quest.description}</b>
                    <p>Difficulty: ${quest.difficulty}</p>
                    <p>Rewards:</p>
                    <ul>
                        <li>Exp: ${quest.experience_reward}</li>
                        <li>Gold: ${quest.currency_reward}</li>
                    </ul>
                    <button>Complete</button>
                `;
                questBoardElement.appendChild(questElement);
            });
        }
    } catch (error) {
        handleCommonErrors(error);
    } finally {
        hideLoadingIndicator();
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById("quest-form-modal");
    const btn = document.getElementById("new-quest-btn");
    const span = document.getElementsByClassName("close-btn")[0];
    const form = document.getElementById("quest-form");

    // Open the modal when the button is clicked
    btn.onclick = function() {
        modal.style.display = "block";
    }

    // Close the modal when the close button is clicked
    span.onclick = function() {
        modal.style.display = "none";
    }

    // Close the modal when clicking outside of the modal
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    // Handle form submission
    form.addEventListener('submit', async function(event) {
        event.preventDefault(); // Prevent the form from submitting the default way

        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        try {
            const response = await fetch('http://127.0.0.1:5000/api/quests', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            if (response.ok) {
                alert('Quest created successfully!');
                modal.style.display = "none"; // Close the modal
                form.reset(); // Reset the form fields
                // Reload the quests
                document.dispatchEvent(new Event('DOMContentLoaded'));
            } else {
                alert('Failed to create quest');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Failed to create quest');
        }
    });
});
