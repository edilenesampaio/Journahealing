const travel_forms = document.querySelectorAll('.save_travel_journal');
for(const form of travel_forms) 
    form.addEventListener('submit', (evt) => {
    evt.preventDefault(); 

    // const formAnswer = {
    //     content: form.querySelector('#travel_journal_content').value,
    //     // date_time: form.querySelector('#save_date_time').value,
    //     address: form.querySelector('#save_address').value,
    // };
 
const formData = new FormData();

formData.append("content", form.querySelector('#travel_journal_content').value)
formData.append("address", form.querySelector('#save_address').value)
const image = form.querySelector('#image')
formData.append("image", image.files[0]);


    fetch('/save_travel_journal', {
        method: 'POST',
        body: formData,
    //     headers: {
    //         'Content-Type': 'application/json'
    //     }
    })

    .then((response) => response.json())
    .then((responseJSON) => {
        form.insertAdjacentHTML(
        alert('Travel Journal Successfully Saved!'),
        window.location.href = '/profile')
    })
    })