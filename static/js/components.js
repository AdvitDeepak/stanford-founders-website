/**
 * components.js: loads shared header/footer, marks the active nav link,
 * and wires the contact form to the intake inbox endpoint.
 */
(function () {
  function load(placeholderId, file) {
    var el = document.getElementById(placeholderId);
    if (!el) return Promise.resolve();
    return fetch(file, { cache: 'no-cache' })
      .then(function (r) { return r.text(); })
      .then(function (html) { el.innerHTML = html; });
  }

  function activeLink() {
    var page = (document.body.dataset.page || '').toLowerCase();
    if (!page) return;
    var links = document.querySelectorAll('nav.primary .links a');
    links.forEach(function (a) {
      if ((a.dataset.page || '').toLowerCase() === page) {
        a.classList.add('active');
      }
    });
  }

  function wireNavToggle() {
    var nav = document.querySelector('nav.primary');
    var toggle = nav && nav.querySelector('.nav-toggle');
    if (!toggle) return;

    function setOpen(open) {
      nav.classList.toggle('open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    }

    toggle.addEventListener('click', function () {
      setOpen(!nav.classList.contains('open'));
    });
    // Tapping a link, pressing Escape, or tapping outside closes the menu.
    nav.addEventListener('click', function (e) {
      if (e.target.closest && e.target.closest('.links a')) setOpen(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') setOpen(false);
    });
    document.addEventListener('click', function (e) {
      if (nav.classList.contains('open') && !nav.contains(e.target)) setOpen(false);
    });
  }

  // Set in contact.html. Points at the club inbox's public contact route.
  var FORM_ENDPOINT = window.SFS_FORM_ENDPOINT || '';

  function wireContactForm() {
    var form = document.getElementById('contact-form');
    if (!form) return;
    var status = form.querySelector('.form-status');
    var btn = form.querySelector('button[type="submit"]');
    var originalLabel = btn ? btn.textContent : 'Send';

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!FORM_ENDPOINT) {
        status.textContent = 'Form endpoint not configured. Email hello@intake.stanfordfoundersclub.com instead.';
        status.className = 'form-status err';
        return;
      }
      status.textContent = 'Sending…';
      status.className = 'form-status';
      if (btn) { btn.disabled = true; btn.textContent = 'Sending…'; }

      var data = new FormData(form);
      var payload = {};
      data.forEach(function (v, k) { payload[k] = v; });

      fetch(FORM_ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      })
        .then(function (r) {
          if (r.ok) return;
          return r.json().catch(function () { return {}; }).then(function (j) {
            throw new Error(j.error || 'Request failed');
          });
        })
        .then(function () {
          status.textContent = 'Sent. We\'ll be in touch.';
          status.className = 'form-status ok';
          form.reset();
          if (btn) { btn.textContent = 'Sent'; }
          setTimeout(function () {
            if (btn) { btn.disabled = false; btn.textContent = originalLabel; }
          }, 2000);
        })
        .catch(function (err) {
          status.textContent = (err && err.message ? err.message + '. ' : 'Error. ') +
            'Try again, or email hello@intake.stanfordfoundersclub.com.';
          status.className = 'form-status err';
          if (btn) { btn.disabled = false; btn.textContent = 'Try again'; }
        });
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    Promise.all([
      load('header-placeholder', 'header.html'),
      load('footer-placeholder', 'footer.html')
    ]).then(function () {
      activeLink();
      wireNavToggle();
      wireContactForm();
    });
  });
})();
