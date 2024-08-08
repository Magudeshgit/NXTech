const navbutton = document.querySelector('.navbutton')
const navexit = document.querySelector('.navexit')
const mobileview = document.querySelector('.mobileview')

navbutton.addEventListener('click', ()=>{
    mobileview.classList.toggle('active')
})
navexit.addEventListener('click', ()=>{
    mobileview.classList.toggle('active')
})