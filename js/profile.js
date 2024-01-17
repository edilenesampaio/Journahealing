const form = document.querySelector(‘#create_journal’);
const h2 = document.querySelector('#journal');

form.addEventListener('submit', (evt) => {
    evt.preventDefault();

    const formAnswer = {
        new_journal: document.querySelector(‘#journal).value
    };

    fetch(‘/create_journal’, {
        methods: 'POST',
        body: JSON.stringify(formAnswer),
        headers: {
            'Content-Type': 'application/json'
        },
    })

    .then((response) => response.json())
    .then((responseJSON) => {
        h2.innerHTML = responseJSON[‘journal’];
    })
})