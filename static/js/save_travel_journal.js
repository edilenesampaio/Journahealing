const forms = document.querySelectorAll('.save_travel_journal');
for(const form of forms) 
    form.addEventListener('submit', (evt) => {
    evt.preventDefault(); 

    const formAnswer = {
        content: form.querySelector('#save_content').value,
        // save_date_time: form.querySelector('#save_date_time').value,
    };
 
    fetch('/save_travel_journal', {
        method: 'POST',
        body: JSON.stringify(formAnswer),
        headers: {
            'Content-Type': 'application/json'
        }
    })

    .then((response) => response.json())
    .then((responseJSON) => {
        form.insertAdjacentHTML(
        alert('Travel Journal Successfully Saved!'),
        window.location.href = '/profile')
    })
    })