const menuToggle = document.getElementById("menu-toggle");
const siteNav = document.getElementById("site-nav");

if (menuToggle && siteNav) {
  menuToggle.addEventListener("click", () => {
    siteNav.classList.toggle("open");
  });
}

const lightbox = document.getElementById("lightbox");
const lightboxImg = document.getElementById("lightbox-img");
const lightboxClose = document.getElementById("lightbox-close");
const lightboxPrev = document.getElementById("lightbox-prev");
const lightboxNext = document.getElementById("lightbox-next");

const clickableImages = Array.from(document.querySelectorAll(".gallery-image, .home-photo"));

let currentImageIndex = 0;

function openLightbox(index) {
  currentImageIndex = index;
  lightboxImg.src = clickableImages[currentImageIndex].src;
  lightboxImg.alt = clickableImages[currentImageIndex].alt;
  lightbox.classList.add("active");
}

function closeLightbox() {
  lightbox.classList.remove("active");
}

function showNextImage() {
  currentImageIndex = (currentImageIndex + 1) % clickableImages.length;
  lightboxImg.src = clickableImages[currentImageIndex].src;
  lightboxImg.alt = clickableImages[currentImageIndex].alt;
}

function showPrevImage() {
  currentImageIndex = (currentImageIndex - 1 + clickableImages.length) % clickableImages.length;
  lightboxImg.src = clickableImages[currentImageIndex].src;
  lightboxImg.alt = clickableImages[currentImageIndex].alt;
}

clickableImages.forEach((img, index) => {
  img.addEventListener("click", () => {
    openLightbox(index);
  });
});

if (lightboxClose) {
  lightboxClose.addEventListener("click", closeLightbox);
}

if (lightboxNext) {
  lightboxNext.addEventListener("click", (e) => {
    e.stopPropagation();
    showNextImage();
  });
}

if (lightboxPrev) {
  lightboxPrev.addEventListener("click", (e) => {
    e.stopPropagation();
    showPrevImage();
  });
}

if (lightbox) {
  lightbox.addEventListener("click", (e) => {
    if (e.target === lightbox) {
      closeLightbox();
    }
  });
}

document.addEventListener("keydown", (e) => {
  if (!lightbox.classList.contains("active")) return;

  if (e.key === "Escape") {
    closeLightbox();
  }

  if (e.key === "ArrowRight") {
    showNextImage();
  }

  if (e.key === "ArrowLeft") {
    showPrevImage();
  }
});
