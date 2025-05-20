async function loadProducts() {
    try {
    const response = await fetch('https://fakestoreapi.com/products');
    const products = await response.json();
    
    const container = document.getElementById("products-container");
    container.innerHTML = products.map(product => `
        <div style="border: 1px solid #ccc; padding: 10px; margin: 10px;">
        <h3>${product.title}</h3>
        <p>ფასი: $${product.price}</p>
        <img src="${product.image}" width="100">
        </div>
    `).join('');
    } catch (error) {
    console.error("error:", error);
    }
}