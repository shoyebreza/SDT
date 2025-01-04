

/* # 4. inputed year is leap year or not  */

var year = 2024;

if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {
    console.log(year + " is a Leap Year.");
} else {
    console.log(year + " is NOT a Leap Year.");
}
