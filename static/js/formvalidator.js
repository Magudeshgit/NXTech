const submit  = document.querySelector('.submitbtn')
const form = document.querySelector('.form')
const email = document.querySelectorAll('.email')

const errortext = document.querySelector('.errortext')

submit.addEventListener('click', (e)=>{
    e.preventDefault()
    
    const pattern = /^7276\d{2}[a-z]{3}\d{3}@mcet\.in$/;
    email.forEach((e)=>{
        if (pattern.test(e.value))
            {
                form.submit()
            }
            else
            {
                errortext.innerText = "Invalid College mail, please enter your official college mail ID"
            }
        
    })
})