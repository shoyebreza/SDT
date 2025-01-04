
/* # 9. saving function  */

function monthlySavings(payments, livingCost) {
    if (!Array.isArray(payments) || isNaN(livingCost)) {
        return "invalid input";
    }
    let totalIncome = 0;

    for (let i = 0; i < payments.length; i++) {
        let payment = payments[i];

        if (payment >= 3000) {
            payment -= payment * 0.20;
        }

        totalIncome += payment;
    }

    let savings = totalIncome - livingCost;

    if (savings >= 0) {
        return savings;
    } else {
        return "earn more";
    }
}

// Sample Input
console.log(monthlySavings([1000, 2000, 3000], 5400));
console.log(monthlySavings([1000, 2000, 2500], 5000));
console.log(monthlySavings([900, 2700, 3400], 10000));
console.log(monthlySavings(100,[900,2700,3400]));

