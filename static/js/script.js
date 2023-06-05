// Offcanvas/sidenav 
function openNav() {
    var mySidenav = document.getElementById("mySidenav");
    var main = document.getElementById("main");
    // adjust the page margin by width of sidenav
    if (mySidenav.style.width === "120px") {
        closeNav();
    } else {
        mySidenav.style.width = "120px";
        main.style.marginLeft = "120px";
    }
}
function closeNav() {
    var mySidenav = document.getElementById("mySidenav");
    var main = document.getElementById("main");
    // close and restore page mrgin to 0
    mySidenav.style.width = "0";
    main.style.marginLeft = "0";
}

// Dark theme
var theme = document.getElementById("theme_icon")
// Check if dark mode preference exists in localStorage
var isDarkMode = localStorage.getItem("darkMode");
// Set initial state based on the stored preference
if (isDarkMode === "true") {
    document.body.classList.add("dark_theme");
    theme.innerHTML = "&#xf205;";
    theme.style.color = "whitesmoke";
}
// Toggle dark mode
theme.onclick = function () {
    // Toggle the class on the body
    document.body.classList.toggle("dark_theme");
    // Update the icon and color based on the current state
    if (document.body.classList.contains("dark_theme")) {
        theme.innerHTML = "&#xf205;";
        theme.style.color = "whitesmoke";
        // Store the dark mode preference in localStorage
        localStorage.setItem("darkMode", "true");
    } else {
        theme.innerHTML = "&#xf204;";
        theme.style.color = "#141414";
        // Remove the dark mode preference from localStorage
        localStorage.removeItem("darkMode");
    }
};
