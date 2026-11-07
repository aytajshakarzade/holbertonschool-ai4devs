function calculateTotal(prices) {
    let total = 0;

    for (let i = 0; i < prices.length; i++) {
        total += prices[i];
    }

    return total;
}

function calculateAverage(prices) {
    const total = calculateTotal(prices);
    return total / prices.length;
}

const productPrices = ["100", "200", "300"];

const total = calculateTotal(productPrices);
const average = calculateAverage(productPrices);

console.log("Total:", total);
console.log("Average:", average);
