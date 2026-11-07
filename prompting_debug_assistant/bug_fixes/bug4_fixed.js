function calculateTotal(prices) {
    let total = 0;

    for (let i = 0; i < prices.length; i++) {
        total += Number(prices[i]);
    }

    return total;
}

function calculateAverage(prices) {
    if (prices.length === 0) {
        return 0;
    }

    const total = calculateTotal(prices);
    return total / prices.length;
}

const productPrices = ["100", "200", "300"];

const total = calculateTotal(productPrices);
const average = calculateAverage(productPrices);

console.log("Total:", total);
console.log("Average:", average);

console.assert(total === 600, "Total test failed");
console.assert(average === 200, "Average test failed");

console.log("All tests passed!");
