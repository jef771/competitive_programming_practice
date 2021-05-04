function calculator() {
    var res = document.getElementById('res');
    res.innerHTMl = "aqui";

    var btn0 = document.getElementById('btn0');

    var btn1 = document.getElementById('btn1');

    var btnClr = document.getElementById('btnClr');

    var btnEql = document.getElementById('btnEql');

    var btnSum = document.getElementById('btnSum');

    var btnSub = document.getElementById('btnSub');

    var btnMul = document.getElementById('btnMul');

    var btnDiv = document.getElementById('btnDiv'); 

    btn0.onclick = function() {
        res.innerHTML+='0';
    }

    btn1.onclick = function() {
        res.innerHTML+='1';
    } 

    btnClr.onclick = function() {
        res.innerHTML = "";
    } 

    btnEql.onclick = function() {
        let operators = '+-*/'
        let operator, operand1 = "", operand2 = "";
        let flag = false;
        let equation = res.innerHTML;
        for(var i=0;i<equation.length;i++) {
            if(!flag) {
                if(operators.includes(equation[i])) {
                    operator = equation[i];
                    flag = true;
                } else {
                    operand1+=equation[i]
                }
            } else {
                operand2+=equation[i];
            }
        }

        let ans;
        if(operator == '+') {
            ans = parseInt(operand1, 2) + parseInt(operand2, 2);
            res.innerHTML = ans.toString(2);
        } else if(operator == '-') {
            ans = parseInt(operand1, 2) - parseInt(operand2, 2);
            res.innerHTML = ans.toString(2);
        } else if(operator == '*') {
            ans = parseInt(operand1, 2) * parseInt(operand2, 2);
            res.innerHTML = ans.toString(2);
        } else {
            ans = parseInt(operand1, 2) / parseInt(operand2, 2);
            res.innerHTML = ans.toString(2);
        }

    }

    btnSum.onclick = function() {
        res.innerHTML+='+';
    }

    btnSub.onclick = function() {
        res.innerHTML+='-';
    }

    btnMul.onclick = function() {
        res.innerHTML+='*';
    }

    btnDiv.onclick = function() {
        res.innerHTML+='/';
    }

}