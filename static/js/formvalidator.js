const submit  = document.querySelector('.submitbtn')
const form = document.querySelector('.form')

const email = document.querySelectorAll('.email')
const contact = document.querySelector('.contact')

const errortext = document.querySelector('.errortext')
const errorhelp = document.querySelector('.errorhelp')

var Flag = true
let EM =''

submit.addEventListener('click', (e)=>{
    e.preventDefault()
    
    const pattern = /^7276\d{2}[a-z]{3}\d{3}@mcet\.in$/;
    email.forEach((e)=>{
        // console.log(e.value)
        if (e.value != '')
            if (!pattern.test(e.value))
            {
                Flag = false
                EM='Invalid College mail, please enter your official college mail ID'
            }   
    })
    
    if (contact.value == '')
    {
        EM = 'Please provide a contact a number'
    }

    if (Flag) form.submit()
    else
    {
        window.scrollTo(0, document.body.scrollHeight)
        errortext.innerText = "Kindly correct the errors" 
        errorhelp.innerText = EM  
    }
})