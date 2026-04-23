document.addEventListener('DOMContentLoaded', () => {
  // Wait until header is loaded
  const checkHeader = setInterval(() => {
    const hamburger = document.querySelector('.hamburger');
    if (hamburger) {
      clearInterval(checkHeader);

      hamburger.addEventListener('click', (e) => {
        e.preventDefault(); // stop instant navigation
        const overlay = document.getElementById('page-fade');
        overlay.style.opacity = '1';

        // Get target from anchor's href
        const targetPage = hamburger.getAttribute('href');

        setTimeout(() => {
          window.location.href = targetPage; // preserves back button
        }, 500);
      });
    }
  }, 50); // keep checking until header exists
});

window.addEventListener('pageshow', () => {
  const overlay = document.getElementById('page-fade');
  if (overlay) {
    overlay.style.opacity = '0';  // reset fade
  }
});