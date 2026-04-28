document.addEventListener('DOMContentLoaded', () => {
    // Load Header
    const headerPlaceholder = document.getElementById('header-placeholder');
    if (headerPlaceholder) {
        fetch('header.html')
            .then(response => response.text())
            .then(data => {
                headerPlaceholder.innerHTML = data;
                setActiveLink();
            })
            .catch(error => console.error('Error loading header:', error));
    }

    // Load Footer
    const footerPlaceholder = document.getElementById('footer-placeholder');
    if (footerPlaceholder) {
        fetch('footer.html')
            .then(response => response.text())
            .then(data => {
                footerPlaceholder.innerHTML = data;
            })
            .catch(error => console.error('Error loading footer:', error));
    }
});

function setActiveLink() {
    // Get the current page filename (e.g., 'about.html')
    let path = window.location.pathname;
    let page = path.split('/').pop();
    
    // Default to index.html if at root
    if (page === '') {
        page = 'index.html';
    }

    // Find the link with the corresponding data-page attribute and style it
    const activeLink = document.querySelector(`.nav-links a[data-page="${page}"]`);
    if (activeLink) {
        activeLink.style.color = 'var(--color-cardinal)';
    }
}
