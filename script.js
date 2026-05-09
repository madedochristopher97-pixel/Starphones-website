document.addEventListener('DOMContentLoaded', () => {
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // Mobile Menu Toggle
    const menuToggle = document.querySelector('.mobile-menu-toggle');
    const mainNav = document.querySelector('.main-nav');

    if (menuToggle && mainNav) {
        menuToggle.addEventListener('click', () => {
            const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
            menuToggle.setAttribute('aria-expanded', !isExpanded);
            mainNav.classList.toggle('active');
        });
    }

    // Hero Image Slider
    const heroSlides = Array.from(document.querySelectorAll('.hero-slide'));
    const heroDots = Array.from(document.querySelectorAll('.hero-slider-dot'));
    let currentHeroSlide = 0;
    let heroSliderTimer;

    const showHeroSlide = (slideIndex) => {
        if (!heroSlides.length) return;

        currentHeroSlide = (slideIndex + heroSlides.length) % heroSlides.length;

        heroSlides.forEach((slide, index) => {
            slide.classList.toggle('is-active', index === currentHeroSlide);
        });

        heroDots.forEach((dot, index) => {
            const isActive = index === currentHeroSlide;
            dot.classList.toggle('is-active', isActive);

            if (isActive) {
                dot.setAttribute('aria-current', 'true');
            } else {
                dot.removeAttribute('aria-current');
            }
        });
    };

    const startHeroSlider = () => {
        if (prefersReducedMotion || heroSlides.length < 2) return;

        window.clearInterval(heroSliderTimer);
        heroSliderTimer = window.setInterval(() => {
            showHeroSlide(currentHeroSlide + 1);
        }, 5000);
    };

    heroDots.forEach((dot) => {
        dot.addEventListener('click', () => {
            showHeroSlide(Number(dot.dataset.slide));
            startHeroSlider();
        });
    });

    showHeroSlide(0);
    startHeroSlider();

    // Scroll Animations (Intersection Observer)
    const animatedElements = document.querySelectorAll('.animate-on-scroll');

    if (!prefersReducedMotion && 'IntersectionObserver' in window) {
        const observerOptions = {
            root: null,
            rootMargin: '0px',
            threshold: 0.15
        };

        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    // Optional: Stop observing once it has become visible
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        animatedElements.forEach(el => {
            observer.observe(el);
        });
    } else {
        // Fallback: If reduced motion is preferred or IntersectionObserver is not supported, 
        // make elements immediately visible
        animatedElements.forEach(el => {
            el.classList.add('is-visible');
        });
    }
});
