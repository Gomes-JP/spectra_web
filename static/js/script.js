// Toggle Sidebar Collapse
const sidebar = document.querySelector('.sidebar');
const toggleButton = document.createElement('div');
toggleButton.classList.add('toggle-button');
toggleButton.innerHTML = '<i class="fa-solid fa-bars"></i>';
document.body.appendChild(toggleButton);

toggleButton.addEventListener('click', () => {
    sidebar.classList.toggle('collapsed');
});

// Highlight Active Page
const currentPage = window.location.pathname;
const links = document.querySelectorAll('.navbar-menu li a');

links.forEach(link => {
    if (link.getAttribute('href') === currentPage) {
        link.parentElement.classList.add('active');
    }
});
