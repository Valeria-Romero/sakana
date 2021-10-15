console.log("Linked")

const splash = document.querySelector('.splash_text');

document.addEventListener('DOMContentLoaded', (e)=>{
    console.log("1")
    setTimeout(()=>{
        splash.classList.add('display-none');
    }, 3000);
})

const splash_img = document.querySelector('.splash_img');

document.addEventListener('DOMContentLoaded', (e)=>{
    console.log("1")
    setTimeout(()=>{
        splash_img.classList.add('display-none');
    }, 3000);
})