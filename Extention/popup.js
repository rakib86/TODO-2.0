document.addEventListener('DOMContentLoaded', function() {
    var openWebsiteButton = document.getElementById('openWebsiteButton');
  
    openWebsiteButton.addEventListener('click', function() {
      chrome.tabs.create({url: 'http://127.0.0.1:8000/'});
    });
  });
  