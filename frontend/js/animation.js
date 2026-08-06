/*==================================
        Animated Counter
===================================*/


const counters =
document.querySelectorAll(".counter");


const counterObserver =
new IntersectionObserver((entries)=>{


entries.forEach(entry=>{


if(entry.isIntersecting){


const counter = entry.target;


const target =
Number(counter.dataset.target);


const suffix =
counter.dataset.suffix || "";


let count = 0;


const duration = 1500;

const increment =
target / (duration / 16);



function updateCounter(){


count += increment;


if(count < target){


counter.textContent =
Math.ceil(count);


requestAnimationFrame(updateCounter);


}else{


counter.textContent =
target + suffix;


}


}


updateCounter();


counterObserver.unobserve(counter);


}


});


});


counters.forEach(counter=>{

counterObserver.observe(counter);

});
/*====================================================
                    6. Scroll Animation
====================================================*/
const hiddenElements = document.querySelectorAll(".hidden");

const observer = new IntersectionObserver((entries) => {

    entries.forEach(entry => {

        if(entry.isIntersecting){

            entry.target.classList.add("show");

        }

    });

});

hiddenElements.forEach(el => observer.observe(el));