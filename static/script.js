// scripts.js

function showPage(pageId) {
    // Hide all sections
    var sections = document.querySelectorAll('.page-content');
    sections.forEach(function(section) {
        section.classList.remove('active');
    });

    // Show the selected section
    var selectedSection = document.getElementById(pageId);
    if (selectedSection) {
        selectedSection.classList.add('active');
    }
}

// Optionally, initialize with the first page visible
document.addEventListener('DOMContentLoaded', function() {
    showPage('characteristics');
});
