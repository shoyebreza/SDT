
/* # 1. grade making*/
/* 0-39 = c 
40-59 = B
60-69 = A-
70-79 = A
80-100 = A+ */

var result = 80;

if (result < 33) {
    console.log("You Failed");
} else if (result >= 33 && result < 40) {
    console.log("Your Result is: C Grade");
} else if (result >= 40 && result < 60) {
    console.log("Your Result is: B Grade");
} else if (result >= 60 && result < 70) {
    console.log("Your Result is: A- Grade");
} else if (result >= 70 && result < 80) {
    console.log("Your Result is: A Grade");
} else if (result >= 80 && result <= 100) {
    console.log("Your Result is: A+ Grade");
} else {
    console.log("Invalid");
}
