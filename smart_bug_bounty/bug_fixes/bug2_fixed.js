function calculateCartTotal(cart) {
    if (!Array.isArray(cart)) {
        throw new TypeError("Cart must be an array");
    }

    let total = 0;

    for (const item of cart) {
        const price = Number(item.price);

        if (!Number.isFinite(price) || price < 0) {
            throw new TypeError("Invalid product price");
        }

        total += price;
    }

    return total;
}

const cart = [
    { name: "Book", price: "15" },
    { name: "Pen", price: "5" },
    { name: "Notebook", price: "10" }
];

console.assert(calculateCartTotal(cart) === 30);
console.assert(calculateCartTotal([]) === 0);

console.log("All bug2 tests passed!");
