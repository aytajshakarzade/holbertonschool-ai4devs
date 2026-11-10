function calculateCartTotal(cart) {
    let total = 0;

    for (let i = 0; i < cart.length; i++) {
        total += cart[i].price;
    }

    return total;
}

const cart = [
    { name: "Book", price: "15" },
    { name: "Pen", price: "5" },
    { name: "Notebook", price: "10" }
];

console.log(calculateCartTotal(cart));
