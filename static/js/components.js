/**
 * components.js: loads shared header/footer, marks the active nav link,
 * and wires the contact form to the Google Apps Script endpoint.
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

  // Apps Script endpoint owns rolling-membership + contact form rows.
  // Update this when the form integration is migrated to the new officer.
  var APPS_SCRIPT_URL = window.SFS_FORM_ENDPOINT || '';

  function wireContactForm() {
    var form = document.getElementById('contact-form');
    if (!form) return;
    var status = form.querySelector('.form-status');
    var btn = form.querySelector('button[type="submit"]');
    var originalLabel = btn ? btn.textContent : 'Send';

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!APPS_SCRIPT_URL) {
        status.textContent = 'Form endpoint not configured. Email stanfordfounders@stanford.edu instead.';
        status.className = 'form-status err';
        return;
      }
      status.textContent = 'Sending…';
      status.className = 'form-status';
      if (btn) { btn.disabled = true; btn.textContent = 'Sending…'; }

      var data = new FormData(form);
      var params = new URLSearchParams();
      data.forEach(function (v, k) { params.append(k, v); });

      fetch(APPS_SCRIPT_URL + '?' + params.toString(), { method: 'GET', mode: 'no-cors' })
        .then(function () {
          status.textContent = 'Sent. We\'ll be in touch.';
          status.className = 'form-status ok';
          form.reset();
          if (btn) { btn.textContent = 'Sent'; }
          setTimeout(function () {
            if (btn) { btn.disabled = false; btn.textContent = originalLabel; }
          }, 2000);
        })
        .catch(function () {
          status.textContent = 'Error. Try again, or email stanfordfounders@stanford.edu.';
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
      wireContactForm();
    });
  });
})();
