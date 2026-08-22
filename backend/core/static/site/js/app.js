// ======================================
// Rohullah Sadat Portfolio
// Main JavaScript File
// ======================================


// Wait until HTML is fully loaded
console.log("APP.JS LOADED");
document.addEventListener("DOMContentLoaded", () => {


    initTheme();

    initMobileMenu();

    initLoader();

    //initReveal();

    //initCounter();

    //initBackToTop();

    //initProjectFilter();

    initGalleryFilter();

    initLightbox();

    

    initScrollProgress();


});



// ======================================
// Dark Mode
// ======================================

function initTheme(){

    const themeButton=document.querySelector(".theme-toggle");

    if(!themeButton) return;


    const savedTheme=localStorage.getItem("theme");


    if(savedTheme==="dark"){

        document.body.classList.add("dark-mode");

    }


    themeButton.addEventListener("click",()=>{

        document.body.classList.toggle("dark-mode");


        const theme =
        document.body.classList.contains("dark-mode")
        ? "dark"
        : "light";


        localStorage.setItem("theme",theme);


    });

}





// ======================================
// Mobile Menu
// ======================================

function initMobileMenu(){


    const menuButton = document.querySelector(".menu-toggle");

    const navbar = document.querySelector(".navbar");


    if(!menuButton || !navbar) return;



    menuButton.addEventListener("click",()=>{


        navbar.classList.toggle("show");


    });


}

// ======================================
// Loader
// ======================================

function initLoader() {

    const loader = document.querySelector("#loader");

    if (!loader) return;

    window.addEventListener("load", () => {

        setTimeout(() => {

            loader.classList.add("hide");

        }, 500);

    });
}



/*====================================================
                    9. Back To Top
====================================================*/

const backToTop = document.getElementById("backToTop");

if(backToTop){

    window.addEventListener("scroll",()=>{

        if(window.scrollY > 400){

            backToTop.classList.add("show");

        }else{

            backToTop.classList.remove("show");

        }

    });

    backToTop.addEventListener("click",()=>{

        window.scrollTo({

            top:0,

            behavior:"smooth"

        });

    });

}



// ======================================
// Project Filter
// ======================================
const categoryButtons = document.querySelectorAll(".filter-btn[data-filter]");
const levelButtons = document.querySelectorAll(".level-btn");

const projectCards = document.querySelectorAll(".project-card");


let selectedCategory = "all";
let selectedLevel = "all";



function filterProjects(){


projectCards.forEach(card=>{


const category = card.dataset.category;
const level = card.dataset.level;



const categoryMatch =
selectedCategory === "all" ||
category === selectedCategory;



const levelMatch =
selectedLevel === "all" ||
level === selectedLevel;



if(categoryMatch && levelMatch){

    card.style.display="block";

}

else{

    card.style.display="none";

}


});


}



// Category Filter

categoryButtons.forEach(button=>{


button.addEventListener("click",()=>{


categoryButtons.forEach(btn=>
    btn.classList.remove("active")
);


button.classList.add("active");


selectedCategory = button.dataset.filter;


filterProjects();


});


});



// Level Filter

levelButtons.forEach(button=>{


button.addEventListener("click",()=>{


levelButtons.forEach(btn=>
    btn.classList.remove("active")
);


button.classList.add("active");


selectedLevel = button.dataset.level;


filterProjects();


});


});

// ======================================
// Gallery Filter
// ======================================

function initGalleryFilter() {

    const galleryButtons =
        document.querySelectorAll(".gallery-btn[data-filter]");

    const galleryImages =
        document.querySelectorAll(".gallery-card[data-category]");

    const videoGallery =
        document.querySelector(".video-gallery");

    if (!galleryButtons.length) return;


    galleryButtons.forEach(button => {

        button.addEventListener("click", () => {

            // Active button
            galleryButtons.forEach(btn => {
                btn.classList.remove("active");
            });

            button.classList.add("active");


            const selectedFilter =
                button.dataset.filter;


            // Filter images
            galleryImages.forEach(card => {

                const category =
                    card.dataset.category;

                if (
                    selectedFilter === "all" ||
                    category === selectedFilter
                ) {

                    card.style.display = "";

                } else {

                    card.style.display = "none";

                }

            });


            // Filter videos
            if (videoGallery) {

                if (
                    selectedFilter === "all" ||
                    selectedFilter === "videos"
                ) {

                    videoGallery.style.display = "";

                } else {

                    videoGallery.style.display = "none";

                }

            }

        });

    });

}
// ======================================
// Gallery Lightbox
// ======================================

function initLightbox(){



    const galleryImages = document.querySelectorAll(".gallery-item img");


    if(!galleryImages.length) return;



}


/*==================================
        Active Navigation
===================================*/

const currentPage = window.location.pathname.split("/").pop();

const navItems = document.querySelectorAll(".nav-list a");

navItems.forEach(link => {

    const href = link.getAttribute("href");

    if(href === currentPage){

        link.classList.add("active");
        const currentPage =
window.location.pathname.split("/").pop() || "index.html";

    }

});

// ======================================
// Scroll Progress
// ======================================

function initScrollProgress(){

    const progressBar =
        document.querySelector("#scroll-progress");

    if(!progressBar) return;


    window.addEventListener("scroll",()=>{

        const scrollTop =
            document.documentElement.scrollTop;

        const scrollHeight =
            document.documentElement.scrollHeight
            -
            document.documentElement.clientHeight;

        const percent =
            (scrollTop / scrollHeight) * 100;

        progressBar.style.width =
            percent + "%";

    });

}
//////////////////////////////////////////////////////
// contact
////========================================================================
const contactForm = document.getElementById("contact-form");

if (contactForm) {

    const submitButton =
        contactForm.querySelector(".contact-submit");

    const submitText =
        contactForm.querySelector(".submit-text");

    const submitLoading =
        contactForm.querySelector(".submit-loading");


    contactForm.addEventListener("submit", function () {

        if (!contactForm.checkValidity()) {
            return;
        }

        submitButton.disabled = true;

        submitText.hidden = true;

        submitLoading.hidden = false;

    });

}