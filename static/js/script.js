// Offcanvas/sidenav 
function openNav() {
    var mySidenav = document.getElementById("mySidenav");
    var main = document.getElementById("main");
    // adjust the page margin by width of sidenav
    if (mySidenav.style.width === "100px") {
        closeNav();
    } else {
        mySidenav.style.width = "100px";
        main.style.marginLeft = "100px";
    }
}
function closeNav() {
    var mySidenav = document.getElementById("mySidenav");
    var main = document.getElementById("main");
    // close and restore page mrgin to 0
    mySidenav.style.width = "0";
    main.style.marginLeft = "0";
}
