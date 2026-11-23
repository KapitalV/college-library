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
    const open = navList.classList.toggle('nav-open');
    document.querySelector('.nav-mobile-toggle').setAttribute('aria-expanded', String(open));
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

  // Separate disclosure buttons keep parent page links usable on touch screens.
  const nav = document.getElementById('mainNavbarList');
  const mobile = window.matchMedia('(max-width: 768px)');
  document.querySelectorAll('#mainNavbarList > li').forEach(function (li, index) {
    const sub = li.querySelector('ul');
    if (!sub) return;
    const link = li.querySelector('a');
    sub.id = 'nav-submenu-' + index;
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'nav-submenu-toggle';
    button.textContent = '+';
    button.setAttribute('aria-label', 'Toggle ' + link.textContent.replace('▼', '').trim() + ' submenu');
    button.setAttribute('aria-controls', sub.id);
    button.setAttribute('aria-expanded', 'false');
    li.insertBefore(button, sub);
    button.addEventListener('click', function () {
      const open = li.classList.toggle('submenu-open');
      button.setAttribute('aria-expanded', String(open));
      button.textContent = open ? '−' : '+';
    });
  });
  function resetNav() {
    if (!nav) return;
    nav.classList.remove('nav-open');
    document.querySelector('.nav-mobile-toggle').setAttribute('aria-expanded', 'false');
    nav.querySelectorAll('.submenu-open').forEach(li => li.classList.remove('submenu-open'));
    nav.querySelectorAll('.nav-submenu-toggle').forEach(button => {
      button.setAttribute('aria-expanded', 'false');
      button.textContent = '+';
    });
  }
  mobile.addEventListener('change', resetNav);
  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && nav && nav.classList.contains('nav-open')) {
      resetNav();
      document.querySelector('.nav-mobile-toggle').focus();
    }
  });
  if (nav) nav.addEventListener('click', function (event) {
    if (mobile.matches && event.target.closest('a')) resetNav();
  });

  // Keep wide data tables independently scrollable, with keyboard access.
  document.querySelectorAll('.content-area table').forEach(function (table) {
    if (table.closest('.table-responsive, .mobile-table-scroll')) return;
    const wrapper = document.createElement('div');
    wrapper.className = 'mobile-table-scroll';
    wrapper.tabIndex = 0;
    wrapper.setAttribute('role', 'region');
    wrapper.setAttribute('aria-label', 'Scrollable data table');
    table.parentNode.insertBefore(wrapper, table);
    wrapper.appendChild(table);
  });
});
