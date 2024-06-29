// script_quests.js

document.addEventListener('DOMContentLoaded', async function() {
    showLoadingIndicator();
    try {
        const quests = await fetchData('http://127.0.0.1:5000/api/quests');
        console.log('quests:', quests);
        const questBoardElement = document.querySelector('.quest-board');
        if (questBoardElement) {
            quests.forEach(quest => {
                const questElement = document.createElement('div');
                questElement.classList.add('quest-item');
                questElement.innerHTML = `
                    <p>${quest.description}</p>
                    <p>Difficulty: ${quest.difficulty}</p>
                    <p>Rewards:</p>
                    <ul>
                        <li>Experience: ${quest.experience}</li>
                        <li>Currency: ${quest.currency}</li>
          a          </ul>
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
