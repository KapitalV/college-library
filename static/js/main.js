/**
 * Government Polytechnic Madhogarh Library
 * Core JavaScript — Live Clock, NDLI Modal, Navigation & Interactions
 */

// 1. Live Date & Time Clock
function updateLiveClock() {
  const clockEl = document.getElementById('live-clock');
  if (!clockEl) return;

  const now = new Date();
  const options = {
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    hour12: true
  };
  clockEl.textContent = now.toLocaleDateString('en-IN', options);
}

// 2. NDLI Club Registration Modal Popup
function openNdliModal() {
  const modal = document.getElementById('ndliModal');
  if (modal) {
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }
}

function closeNdliModal() {
  const modal = document.getElementById('ndliModal');
  if (modal) {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }
}

function handleNdliBackdropClick(event) {
  if (event.target && event.target.id === 'ndliModal') {
    closeNdliModal();
  }
}

// 3. Mobile Navigation Menu Toggle
function toggleMobileNav() {
  const navList = document.getElementById('mainNavbarList');
  if (navList) {
    navList.classList.toggle('nav-open');
  }
}

// 4. Smooth Back-to-Top
function scrollToTop() {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
}

// 5. Initialize on DOM Loaded
document.addEventListener('DOMContentLoaded', function () {
  // Start Clock
  updateLiveClock();
  setInterval(updateLiveClock, 1000);

  // Close NDLI Modal on Escape key
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      closeNdliModal();
    }
  });

  // Back to Top button scroll handler
  const backToTopBtn = document.getElementById('back-to-top');
  if (backToTopBtn) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 250) {
        backToTopBtn.classList.add('visible');
      } else {
        backToTopBtn.classList.remove('visible');
      }
    });
  }

  // Pure CSS mobile submenu touch helper
  const hasSubItems = document.querySelectorAll('.nav-bar li');
  hasSubItems.forEach(function (li) {
    const sub = li.querySelector('ul');
    if (sub) {
      const link = li.querySelector('a');
      if (link && window.innerWidth <= 768) {
        link.addEventListener('click', function (e) {
          if (sub.style.display !== 'block') {
            e.preventDefault();
            sub.style.display = 'block';
          } else {
            sub.style.display = '';
          }
        });
      }
    }
  });
});
