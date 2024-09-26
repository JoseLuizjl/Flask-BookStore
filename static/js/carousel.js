let currentIndex = 0;
const books = document.querySelectorAll('.book');
const totalBooks = books.length;
const booksPerView = 4;

function moveSlide(direction) {
    const slideWrapper = document.querySelector('.carousel-slide');
    currentIndex += direction;

    if (currentIndex < 0) {
        currentIndex = Math.ceil(totalBooks / booksPerView) - 1;
    } else if (currentIndex >= Math.ceil(totalBooks / booksPerView)) {
        currentIndex = 0;
    }

    slideWrapper.style.transform = `translateX(${-currentIndex * 100}%)`;
    updateDots();
}

function updateDots() {
    const dots = document.querySelectorAll('.dot');
    dots.forEach(dot => dot.classList.remove('active'));
    dots[currentIndex].classList.add('active');
}

function currentSlide(index) {
    currentIndex = index - 1;
    const slideWrapper = document.querySelector('.carousel-slide');
    slideWrapper.style.transform = `translateX(${-currentIndex * 100}%)`;
    updateDots();
}

updateDots();
