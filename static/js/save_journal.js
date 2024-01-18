const forms = document.querySelectorAll('.save_journal’);
for(const form of forms) {
    form.addEventListener('submit', (evt) => {
    evt.preventDefault(); 

    const formAnswer = {
        save_content: form.querySelector('#save_content’).value,
    };
 
    fetch('/save_journal’, {
        method: 'POST',
        body: JSON.stringify(formAnswer),
        headers: {
            'Content-Type': 'application/json'
        }
    })

    .then((response) => response.json())
    .then((responseJSON) => {
        form.insertAdjacentHTML(
        alert(‘Your Journal Is Saved!’),
        window.location.href = '/profile')
    })

});

