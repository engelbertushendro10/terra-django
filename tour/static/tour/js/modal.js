
  const images = [
    "./assets/images/rangko/1.png",
    "./assets/images/rangko/2.png",
    "./assets/images/rangko/3.png",
  ];
  let currentIndex = 0;

  function toggleModal() {
    const modal = document.getElementById('photoModal');
    modal.classList.toggle('hidden');
    document.getElementById('sliderImage').src = images[currentIndex];
  }

  function nextImage() {
    currentIndex = (currentIndex + 1) % images.length;
    document.getElementById('sliderImage').src = images[currentIndex];
  }

  function prevImage() {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    document.getElementById('sliderImage').src = images[currentIndex];
  }