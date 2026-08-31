/* ═══════════════════════════════════════
   SWEDE SAUNA v4 — main.js
   ═══════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', () => {

  // Nav scroll state
  const nav = document.getElementById('nav');
  const onScroll = () => nav.classList.toggle('is-scrolled', window.scrollY > 20);
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Hamburger
  const burger  = document.getElementById('burger');
  const navMenu = document.getElementById('navMenu');
  if (burger && navMenu) {
    burger.addEventListener('click', () => {
      const open = navMenu.classList.toggle('is-open');
      burger.classList.toggle('is-open', open);
      document.body.style.overflow = open ? 'hidden' : '';
    });
    navMenu.querySelectorAll('a').forEach(a =>
      a.addEventListener('click', () => {
        navMenu.classList.remove('is-open');
        burger.classList.remove('is-open');
        document.body.style.overflow = '';
      })
    );
  }

  // Reveal on scroll
  const reveals = document.querySelectorAll('.reveal');
  if (reveals.length) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e, i) => {
        if (e.isIntersecting) {
          // Slight stagger between siblings
          const siblings = [...(e.target.parentNode?.children || [])].filter(el => el.classList.contains('reveal'));
          const idx = siblings.indexOf(e.target);
          e.target.style.transitionDelay = `${Math.min(idx, 5) * 90}ms`;
          e.target.classList.add('is-visible');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    reveals.forEach(el => io.observe(el));
  }

  // Smooth anchor scrolling with nav offset
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    const href = a.getAttribute('href');
    if (href.length > 1) {
      a.addEventListener('click', (e) => {
        const target = document.querySelector(href);
        if (target) {
          e.preventDefault();
          const navH = document.getElementById('nav').offsetHeight;
          const top = target.getBoundingClientRect().top + window.scrollY - navH - 16;
          window.scrollTo({ top, behavior: 'smooth' });
        }
      });
    }
  });

});
