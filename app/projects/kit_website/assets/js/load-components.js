async function loadComponent(id, htmlPath, cssPath = null) {
    try {
        // Load HTML
        const res = await fetch(htmlPath);
        const html = await res.text();
        document.getElementById(id).innerHTML = html;

        // Load CSS if provided
        if (cssPath) {
            const link = document.createElement("link");
            link.rel = "stylesheet";
            link.href = cssPath;
            document.head.appendChild(link);
        }
    } catch (err) {
        console.error(`Failed to load component ${id}:`, err);
    }
}

// Check if the current page is in the 'pages' folder or the root
const isSubPage = window.location.pathname.includes('/pages/');
const prefix = isSubPage ? '../' : '';

// Use the prefix to make the paths dynamic
// Load footer/header with its CSS
loadComponent("header-container", `${prefix}components/header.html`, `${prefix}assets/css/pages/header.css`);
loadComponent("footer-container", `${prefix}components/footer.html`, `${prefix}assets/css/pages/footer.css`);