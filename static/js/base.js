(function () {
  'use strict';

  window.onload = activeLinkForNav;

  function activeLinkForNav() {
    let navElement = document.getElementById('navbar');
    let ulElements = navElement.getElementsByClassName('nav navbar-nav');
    let url = window.location.pathname;
    for (let ulElement of ulElements) {
      let liElements = ulElement.children;
      for (let li of liElements) {
        if (li.children[0].getAttribute('href') === url) {
          li.className = 'active';
          return;
        }
      }
    }
  }

  // flash messages
  $('.alert').on('click', function (e) {
    $(this).slideUp('slow');
  })

  let alertElement = document.getElementsByClassName('alert')[0];
  if (alertElement) {
    setTimeout(function () {
      $('.alert').slideUp('slow');
    }, 3000);
  }
}());
