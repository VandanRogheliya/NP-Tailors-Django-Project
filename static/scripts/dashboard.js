if (document.title == "Dashboard | NP Tailors" || document.title == "Add New Customer | NP Tailors" || document.title == "Edit Measurements | NP Tailors" || document.title == "Customer Measurements | NP Tailors" || document.title == "Reset Password | NP Tailors") {
  $('.nav-menu .active, .mobile-nav .active').removeClass('active');
  $('.dashboardActive').addClass('active');
}

if (document.title == "NP Tailors") {
  $('.nav-menu .active, .mobile-nav .active').removeClass('active');
  $('.homeActive').addClass('active');
}


console.log("Works");