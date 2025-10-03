'use strict';

/**
 * navbar toggle
 */

const overlays = document.querySelector("[data-overlays]");
const navOpenBtn = document.querySelector("[data-nav-open-btns]");
const navbars = document.querySelector("[data-navbars]");
const navCloseBtn = document.querySelector("[data-nav-close-btns]");
const navLinks = document.querySelectorAll("[data-nav-link]");

const navElemArr = [navOpenBtn, navCloseBtn, overlays];

const navToggleEvent = function (elem) {
  for (let i = 0; i < elem.length; i++) {
    elem[i].addEventListener("click", function () {
      navbars.classList.toggle("active");
      overlays.classList.toggle("active");
    });
  }
}

navToggleEvent(navElemArr);
navToggleEvent(navLinks);



/**
 * header sticky & go to top
 */

const headers = document.querySelector("[data-headers]");
// const goTopBtn = document.querySelector("[data-go-top]");

window.addEventListener("scroll", function () {

  if (window.scrollY >= 200) {
    headers.classList.add("active");
    // goTopBtn.classList.add("active");
  } else {
    headers.classList.remove("active");
    // goTopBtn.classList.remove("active");
  }

});