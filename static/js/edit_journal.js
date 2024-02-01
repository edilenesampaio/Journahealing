const editJournalButtons = document.querySelectorAll('button.edit_journals');
for(const editJournalButton of editJournalButtons) {
editJournalButton.addEventListener('click', (evt) => {
    const formAnswer = {
        edit_journal: evt.target.id,
        journal: evt.target.content
    }

    fetch('/edit_journal', {
        method: 'POST',
        body: JSON.stringify(formAnswer),
        headers: {
            'Content-Type': 'application/json'
        },
    })

    .then((response) => response.json())
    .then((responseJSON) => {
        alert('Journal edited')
        window.location.href = `/journal/${responseJSON.journal_id}`
    })
});
}
