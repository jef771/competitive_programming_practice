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
         
    function b(s) {
        let even = 0;
        let odd = 0;
        for(let i=0;i<s.length;i++) {
            if(i%2==0) {
                if(s[i] === s[i].toLowerCase()) {
                    even++;
                }
            } else {
                if(s[i] == s[i].toUpperCase()) {
                    odd++;
                }
            }
        }
        
     
        if(even+odd === s.length) {
            return 'Yes';
        } else {
            return 'No';
        }
    }
         
    function main() {
        var s = readLine();
        
        console.log(b(s));
    }