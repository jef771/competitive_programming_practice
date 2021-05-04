process.stdin.setEncoding('utf-8')
let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {

        return string.trim();
    });
    
    main();  
});

function readLine() {
    return inputString[currentLine++];
}

function star(x) {
    
    if(x%100>0) {
        let temp = x%100;
        let ans = 100 - temp;
        return ans;
    } else {
        return 100;
    }
}

function main() {
    const x = +(readLine());
    
    console.log(star(parseInt(x)));
}
