// ======================================
// Rohullah Sadat Portfolio
// Animation JavaScript
// ======================================

document.addEventListener("DOMContentLoaded", () => {

    initCounterAnimation();
    initScrollAnimation();

});


// ======================================
// Animated Counter
// ======================================

function initCounterAnimation() {

    const counters = document.querySelectorAll(".counter");

    if (!counters.length) return;

    const counterObserver = new IntersectionObserver((entries) => {

        entries.forEach(entry => {

            if (!entry.isIntersecting) return;

            const counter = entry.target;

            const target = Number(
                counter.dataset.target || 0
            );

            const suffix =
                counter.dataset.suffix || "";

            let count = 0;

            const duration = 1500;

            const increment =
                target / (duration / 16);


            function updateCounter() {

                count += increment;

                if (count < target) {

                    counter.textContent =
                        Math.ceil(count);

                    requestAnimationFrame(
                        updateCounter
                    );

                } else {

                    counter.textContent =
                        target + suffix;

                }

            }


            updateCounter();

            counterObserver.unobserve(counter);

        });

    });


    counters.forEach(counter => {

        counterObserver.observe(counter);

    });

}


// ======================================
// Scroll Animation
// ======================================

function initScrollAnimation() {

    const hiddenElements =
        document.querySelectorAll(".hidden");

    if (!hiddenElements.length) return;


    const observer = new IntersectionObserver(
        (entries) => {

            entries.forEach(entry => {

                if (entry.isIntersecting) {

                    entry.target.classList.add("show");

                    observer.unobserve(
                        entry.target
                    );

                }

            });

        }
    );


    hiddenElements.forEach(element => {

        observer.observe(element);

    });

}