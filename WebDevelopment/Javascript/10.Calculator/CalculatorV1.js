var storedValue = 0;
var displayValue = 0;
var displayString = "";
var pendingOp = "";
var lastOp = 0;
var resetDisplay = false;
var decimal = false;
var decimalFactor = 1;

function press(num) {
    if (resetDisplay)
        resetDisp();

    displayString = document.querySelector("#display").innerText;

    if (displayString == "UNDEFINED") {
        clr();
        document.querySelector("#display").innerText = num;
        displayValue = num;
    }
    else if (num == ".") {
        if (!decimal) {
            decimal = true;
            // if (displayString==0)
            //     document.querySelector("#display").innerText = "0.";
            // else
            document.querySelector("#display").innerText = displayString + ".";
            decimalFactor /= 10;
        }
        else
            clr();
    }
    else if (displayString == 0) {
        document.querySelector("#display").innerText = num;
        displayValue = num;
    }
    else if (!decimal) {
        document.querySelector("#display").innerText += num;
        displayValue = displayValue*10*decimalFactor + decimalFactor*num;
        console.log("DV" + displayValue);
    }
    else {
        document.querySelector("#display").innerText += num;
        displayValue += decimalFactor*num;
        decimalFactor /= 10;
    }

    displayString = document.querySelector("#display").innerText;
    console.log("PIDS " + parseInt(displayString));
    console.log("DF " + decimalFactor);
    console.log(displayValue);


    // console.log(resetDisplay);
    // if (resetDisplay) {
    //     displayValue = 0;
    //     resetDisplay = false;
    //     console.log("I'm here");
    // }
    // if (document.querySelector("#display").innerText == "UNDEFINED")
    //     displayValue = num;
    // else if (num != ".") {
    //     displayValue = displayValue*10 + num;
    //     document.querySelector("#display").innerText = displayValue;
    //     displayString = displayValue;
    // }
    // else {
    //     displayString = displayValue;
    //     displayString += num;
    // }
    // // displayString=displayValue;
    // document.querySelector("#display").innerText = displayString;
}




function setOp(operator) {
    var displayString = document.querySelector("#display").innerText;
    console.log(storedValue + " " + displayValue + " " + displayString);
    console.log("Operator:" + operator + " PendingOp:"+pendingOp);
    if (pendingOp == "") {
        storedValue = displayValue;
        displayValue = 0;
        console.log("YES " + storedValue + " " + displayValue);
    }
    else {
        calculate();
        console.log("Calculating " + storedValue + pendingOp + displayValue);
    }
        pendingOp = operator;
        console.log(pendingOp);
        resetDisplay = true;
        document.querySelector("#stored-value").innerText = storedValue;
        resetDecimals();
}

function calculate() {
    // calculate
    // need a way to complete operation again if equals sign is hit twice in a row???
    if (pendingOp != "") {
        // var num1 = parseInt(storedValue);
        // var num2 = parseInt(displayValue);
        var num1 = storedValue;
        var num2 = displayValue;
        var result = 0;
        if (pendingOp === "+")
            result = num1+num2;
        else if (pendingOp === "-")
            result = num1-num2;
        else if (pendingOp === "*")
            result = num1*num2;
        else {
            if (num2 == 0)
                return document.querySelector("#display").innerText = "UNDEFINED";
            result = num1/num2;
        }
        // clear pending operation
        pendingOp = "";
        // update stored value
        storedValue = result;
        displayValue = result;
        console.log(storedValue + " " + result + " " + pendingOp);
        // update display value (until next input)
        document.querySelector("#display").innerText = storedValue;
        document.querySelector("#stored-value").innerText = storedValue;
        }
    else
        clr();
}

function clr() {
    resetStoredValues();
    resetOperators();
    resetDecimals();
    resetDisp();
}

function resetStoredValues() {
    document.querySelector("#stored-value").innerText = 0;
    storedValue = 0;
}
function resetOperators() {
    pendingOp = "";
    lastOp = 0;
}
function resetDecimals() {
    decimal = false;
    decimalFactor = 1;
}
function resetDisp() {
    displayString = "";
    displayValue = 0;
    document.querySelector("#display").innerText = 0;
    resetDisplay = false;
}

// function resetCalculator() {
//     document.querySelector("#display").innerText = 0;
//     document.querySelector("#stored-value").innerText = 0;
//     storedValue = 0;
//     pendingOp = "";
//     lastOp = 0;
// }