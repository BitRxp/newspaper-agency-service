// Function to toggle the sidebar
function toggleSidebar() {
    console.log("toggleSidebar called");
    var sidebar = document.getElementById("sidebar");
    sidebar.classList.toggle("active");
    document.body.classList.toggle("sidebar-active");

    // Save the current state to localStorage
    var isActive = sidebar.classList.contains("active");
    localStorage.setItem("sidebarActive", isActive);
}

// Function to restore the sidebar state
function restoreSidebarState() {
    var sidebarActive = localStorage.getItem("sidebarActive");
    var sidebar = document.getElementById("sidebar");

    if (sidebarActive === "true") {
        sidebar.classList.add("active");
        document.body.classList.add("sidebar-active");
    } else {
        sidebar.classList.remove("active");
        document.body.classList.remove("sidebar-active");
    }
}

// Function for asynchronous navigation
function handleNavigation(event, url) {
    event.preventDefault();

    // Update the URL without reloading the page
    history.pushState(null, "", url);

    // Asynchronously load new content
    fetch(url)
        .then(response => response.text())
        .then(data => {
            // Parse the new content
            const parser = new DOMParser();
            const newDocument = parser.parseFromString(data, "text/html");
            const newContent = newDocument.querySelector(".container-content").innerHTML;

            // Update only the content container
            document.querySelector(".container-content").innerHTML = newContent;

            // After loading new content, restore the sidebar state
            restoreSidebarState();
        })
        .catch(error => console.error("Error fetching content:", error));
}

// Function to delegate click events
function setupGlobalClickHandler() {
    document.addEventListener("click", function(event) {
        let target = event.target;

        // Check if the sidebar toggle button or its child was clicked
        if (target.closest("#sidebarToggle")) {
            toggleSidebar();
            event.preventDefault();
            return;
        }

        // Find the closest <a> or <button> element
        target = event.target.closest("a, button");

        if (!target) return;

        // If it's a link
        if (target.tagName.toLowerCase() === "a") {
            const url = target.getAttribute("href");
            // Check if it's an internal link
            if (url && url.startsWith("/")) {
                handleNavigation(event, url);
            }
        }

        // If it's a button
        if (target.tagName.toLowerCase() === "button") {
            const url = target.getAttribute("data-url");
            if (url) {
                handleNavigation(event, url);
            }
        }
    });
}

// After the page loads, set up event handlers
window.addEventListener("load", function() {
    restoreSidebarState();
    document.body.classList.add("loaded");
    setupGlobalClickHandler();
});
