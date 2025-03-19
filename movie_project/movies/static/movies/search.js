// search.js
document.getElementById('search-bar').addEventListener('input', function() {
    let searchQuery = this.value.toLowerCase();
    let movieItems = document.querySelectorAll('.movie-item');
    let noResults = document.getElementById('no-results');
    let hasResults = false;

    movieItems.forEach(function(item) {
        let title = item.querySelector('h2').innerText.toLowerCase();
        if (title.includes(searchQuery)) {
            item.style.display = '';
            hasResults = true;
        } else {
            item.style.display = 'none';
        }
    });

    if (hasResults) {
        noResults.style.display = 'none';
    } else {
        noResults.style.display = 'block';
    }
});
