document.addEventListener("DOMContentLoaded", function() {
  // Theme switching logic with localStorage support
  const themeSwitch = document.getElementById("theme-switch");
  
  // Set theme on load based on localStorage value
  if (localStorage.getItem("theme") === "light") {
    document.body.classList.remove("dark-theme");
    document.body.classList.add("light-theme");
    themeSwitch.checked = false;
  } else {
    document.body.classList.remove("light-theme");
    document.body.classList.add("dark-theme");
    themeSwitch.checked = true;
  }
  
  themeSwitch.addEventListener("change", function() {
    if (this.checked) {
      document.body.classList.remove("light-theme");
      document.body.classList.add("dark-theme");
      localStorage.setItem("theme", "dark");
    } else {
      document.body.classList.remove("dark-theme");
      document.body.classList.add("light-theme");
      localStorage.setItem("theme", "light");
    }
  });

  // Example logic for a menu toggle if present
  const menuBtn = document.getElementById("menu-btn");
  const menu = document.getElementById("menu");
  if (menuBtn && menu) {
    menuBtn.addEventListener("click", function() {
      menuBtn.classList.toggle("open");
      menu.classList.toggle("open");
    });
  }

  // Example logic for a neon button (e.g., for changing username)
  const neonButton = document.getElementById("neon-button");
  const boxContainer = document.getElementById("box-container");
  if (neonButton && boxContainer) {
    neonButton.addEventListener("mousedown", function() {
      // Add 'change' class for animation
      boxContainer.classList.add("change");
      setTimeout(function() {
        // Revert to default class after animation (assumes default is "center")
        boxContainer.className = "center";
      }, 1000);
    });
  }
});