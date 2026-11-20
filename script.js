document.addEventListener("DOMContentLoaded", () => {
  // Mobile menu
  const menuToggle = document.getElementById("menuToggle");
  const navLinks = document.getElementById("navLinks");
  if (menuToggle && navLinks) {
    menuToggle.addEventListener("click", () => navLinks.classList.toggle("open"));
  }

  // Swipe photo carousel (home page)
  const carousel = document.getElementById("photoCarousel");
  const dots = document.querySelectorAll("#carouselDots .dot");
  if (carousel && dots.length) {
    carousel.addEventListener("scroll", () => {
      const index = Math.round(carousel.scrollLeft / carousel.clientWidth);
      dots.forEach((d, i) => d.classList.toggle("active", i === index));
    });
    dots.forEach((d, i) =>
      d.addEventListener("click", () =>
        carousel.scrollTo({ left: i * carousel.clientWidth, behavior: "smooth" })
      )
    );
  }
});