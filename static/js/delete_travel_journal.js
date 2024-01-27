const deleteJournalButtons = document.querySelectorAll('button.delete_travel_journals');
for(const deleteTravel_JournalButton of deleteTravel_JournalButtons) {
deleteTravel_JournalButton.addEventListener('click', (evt) => {
    const formAnswer = {
        delete_travel_journal: evt.target.id,
        travel_journal: evt.target.content
    }

    fetch('/delete_travel_journal', {
        method: 'POST',
        body: JSON.stringify(formAnswer),
        headers: {
            'Content-Type': 'application/json'
        },
    })

    .then((response) => response.json())
    .then((responseJSON) => {
        alert('Travel Journal deleted')
        window.location.href = `/travel_journal/${responseJSON.travel_journal_id}`
    })
});
}
