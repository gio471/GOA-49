document.getElementById('searchForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const searchTerm = document.getElementById('searchInput').value.trim();
    if (searchTerm) {
        searchBooks(searchTerm);
    }
});

function searchBooks(searchTerm) {
    const resultsContainer = document.getElementById('resultsContainer');
    resultsContainer.innerHTML = '<div class="loading">starting search...</div>';
    fetch(`https://www.googleapis.com/books/v1/volumes?q=${encodeURIComponent(searchTerm)}`)
        .then(response => response.json())
        .then(data => {
            displayResults(data.items || []);
        })
        .catch(error => {
            console.error('Error fetching data:', error);
            resultsContainer.innerHTML = '<div class="no-results">there was error during getting date. please try again.</div>';
        });
}
function displayResults(books) {
    const resultsContainer = document.getElementById('resultsContainer');
    if (books.length === 0) {
        resultsContainer.innerHTML = '<div class="no-results">book can not search. try other word.</div>';
        return;
    }

    resultsContainer.innerHTML = '';
    books.forEach(book => {
        const volumeInfo = book.volumeInfo || {};
        const imageLinks = volumeInfo.imageLinks || {};
        
        const bookCard = document.createElement('div');
        bookCard.className = 'book-card';
        
        bookCard.innerHTML = `
            <img src="${imageLinks.thumbnail || 'https://via.placeholder.com/150x200?text=No+Cover'}" alt="${volumeInfo.title || 'Unknown'}" class="book-cover">
            <div class="book-info">
                <h3 class="book-title">${volumeInfo.title || 'Title is unknown'}</h3>
                <div class="book-meta">
                    ${volumeInfo.publishedDate ? `print date: ${volumeInfo.publishedDate.substring(0,4)}` : ''}
                    ${volumeInfo.pageCount ? ` | pages: ${volumeInfo.pageCount}` : ''}
                </div>
                <p class="book-description">${volumeInfo.description || 'Description is not available.'}</p>
            </div>
        `;
resultsContainer.appendChild(bookCard);
});
}
