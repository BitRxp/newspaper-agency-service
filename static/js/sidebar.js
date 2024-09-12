document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.getElementById('sidebar');
    const sidebarToggle = document.getElementById('sidebarToggle');

    if (localStorage.getItem('sidebarActive') === 'true') {
        sidebar.classList.add('active');
    }

    sidebarToggle.addEventListener('click', function() {
        sidebar.classList.toggle('active');
        if (sidebar.classList.contains('active')) {
            localStorage.setItem('sidebarActive', 'true');
        } else {
            localStorage.setItem('sidebarActive', 'false');
        }
    });
});
