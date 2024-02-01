const editTravel_JournalButtons = document.querySelectorAll('button.edit_travel_journals');
for(const editTravel_JournalButton of editTravel_JournalButtons) {
editTravel_JournalButton.addEventListener('click', (evt) => {
    const formAnswer = {
        edit_travel_journal: evt.target.id,
        travel_journal: evt.target.content
    }

    fetch('/edit_travel_journal', {
        method: 'POST',
        body: JSON.stringify(formAnswer),
        headers: {
            'Content-Type': 'application/json'
        },
    })

    .then((response) => response.json())
    .then((responseJSON) => {
        alert('Travel Journal edited')
        window.location.href = `/travel_journal/${responseJSON.travel_journal_id}`
    })
});
}
