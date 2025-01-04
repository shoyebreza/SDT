
/* # 3. Sorting number  */


var array = [12, 5, 20, 1, 7, 15, 3, 10, 8, 18, 2, 6, 19, 4, 13, 17, 14, 9, 16, 11];

/* console.log(array.sort()); */

// Sorting in ascending order
array.sort(function(a, b) {
    return a - b;
});
console.log("Sorted Array in Ascending Order: ", array);

// Sorting in descending order
/* array.sort(function(a, b) {
    return b - a;
});
console.log("Sorted Array in Descending Order: ", array);
 */

