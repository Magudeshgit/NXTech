const submit  = document.querySelector('.submitbtn')
const form = document.querySelector('.form')

const email = document.querySelectorAll('.email')
const m1 = document.querySelector('.m1')
const contact = document.querySelector('.contact')

const errortext = document.querySelector('.errortext')
const errorhelp = document.querySelector('.errorhelp')
let EM =''

submit.addEventListener('click', (e)=>{
    var Flag = true
    e.preventDefault()
    console.log("CHecking", m1.value)
    const pattern = /^7276\d{2}[a-z]{3}\d{3}@mcet\.in$/;
    email.forEach((e)=>{
        // console.log(e.value)
        if (e.value != '')
        {
            if (!pattern.test(e.value))
            {
                Flag = false
                EM='Invalid College mail, please enter your official college mail ID'
            }   
        }
        
    })
    console.log(contact.value)
    if (contact.value == '')
    {
        console.log("cv",contact.value)
        Flag = false
        EM = "Please provide a contact a number"
    }
    if (m1.value == '')
    {
        Flag = false
        console.log(m1.value)
        EM = "Please fill mail id of participant1"
    }

    if (Flag) form.submit()
    else
    {
        window.scrollTo(0, document.body.scrollHeight)
        errortext.innerText = "Kindly correct the errors" 
        errorhelp.innerText = EM  
    }
})
