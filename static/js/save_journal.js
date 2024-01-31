const forms = document.querySelectorAll('.save_journal');
for(const form of forms) 
    form.addEventListener('submit', (evt) => {
    evt.preventDefault(); 

    const formAnswer = {
        content: form.querySelector('#journal_content').value,
        // save_date_time: form.querySelector('#save_date_time').value,
    };
 
    fetch('/save_journal', {
        method: 'POST',
        body: JSON.stringify(formAnswer),
        headers: {
            'Content-Type': 'application/json'
        }
    })

    .then((response) => response.json())
    .then((responseJSON) => {
        alert('Journal Successfully Saved!');
        document.querySelector('#journal_list').insertAdjacentHTML('beforeend', `<li>
        <a href="/journal/${responseJSON.journal_id}"> ${responseJSON.content} ${responseJSON.created_at}</a>
         </li>`)
        form.querySelector('#journal_content').value=''
    })
    })






