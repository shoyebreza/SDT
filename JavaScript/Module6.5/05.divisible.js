
/* # 5. 3 & 5 divisible number */

var divisible = [];

for (var i = 1; i <= 50; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
        divisible.push(i);
    }
}

console.log(divisible);

