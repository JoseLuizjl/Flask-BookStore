var swiper = new Swiper(".swiper", {
    cssMode: true,
    loop: true,
    slidesPerView: 4,
    spaceBetween: 10, 
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    keyboard: true,
});
