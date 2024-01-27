const deleteJournalButtons = document.querySelectorAll('button.delete_journals');
for(const deleteJournalButton of deleteJournalButtons) {
deleteJournalButton.addEventListener('click', (evt) => {
    const formAnswer = {
        delete_journal: evt.target.id,
        journal: evt.target.content
    }

    fetch('/delete_journal', {
        method: 'POST',
        body: JSON.stringify(formAnswer),
        headers: {
            'Content-Type': 'application/json'
        },
    })

    .then((response) => response.json())
    .then((responseJSON) => {
        alert('Journal deleted')
        window.location.href = `/journal/${responseJSON.journal_id}`
    })
});
}
