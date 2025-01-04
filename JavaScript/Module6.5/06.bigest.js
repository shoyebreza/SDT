

/* # 6.bigest friend name */

var friends = ["rahim", "karim", "abdul", "sadsd", "heroAlom"];
var bigName = "";

for (var i = 0; i < friends.length; i++) {
    if (friends[i].length > bigName.length) {
        bigName = friends[i];
    }
}

console.log("The longest name is:", bigName);


