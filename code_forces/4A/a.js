const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

function watermelon(x) {

    if(x > 2 && x%2===0) {
        return 'YES';
    } else {
        return 'NO';
    }
} 

readline.question("", (x) => {
    console.log(watermelon(parseInt(x)));
    readline.close();
});
 