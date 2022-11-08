// Global Variables
var clearNextPress = false;
var dispVal = 0;
var dispStr = "";
var storageVal = 0;
var isReset = true;
var isDisplayReset = true;
var needResetDisplay = false;
var isDecimal = false;
var decimalFactor = 0.1;
var pendingOp = "";
var lastOp = [];
var lastInput = 0; // (2 for calculate, 1 for number, 0 for operation or decimal)
var unresolvedOp = false;

function press(num) {
    if (clearNextPress)
        return clr();
    if (needResetDisplay) { // Triggered if last input was operation (+, -, *, /)
        document.querySelector("#display").innerText = 0;
        needResetDisplay = false;
    }
    if (lastInput == 2) { // Last input was "="
        clr();
        isReset = false;
        isDisplayReset = false;
        needResetDisplay = false;
        if (num==".") {
            console.log(".");
            isDecimal = true;
            lastInput = 0;
            return document.querySelector("#display").innerText = "0.";
        }
        else {
            console.log("num");
            dispVal = num;
            lastInput = 1;
            return document.querySelector("#display").innerText = num;
        }
    }
    if (isReset) // Only triggered at start of program or if "c" is pressed
        if (num != 0) {
            isReset = false;
            isDisplayReset = false;
            if (num == ".") {
                console.log(".");
                isDecimal = true;
                lastInput = 0;
                return document.querySelector("#display").innerText = "0.";
            }
            else { // Input 1-9
                console.log("1-9");
                dispVal = num;
                lastInput = 1;
                return document.querySelector("#display").innerText = num;
            }
        } else {
            return lastInput = 1;
        }
    if (document.querySelector("#display").innerText == "0" && num!=".") {
        console.log("issue");
        document.querySelector("#display").innerText = num;
        dispVal = num;
    } else {
        if (num == ".") {
            if (isDecimal) { // If already a decimal -> RESET
                console.log("Error. Cannot Select Decimal Twice");
                return clr();
            } else { // If not already a decimal -> Trigger Decimal Protocol
                isDecimal = true;
                document.querySelector("#display").innerText += num;
            }
        } else { // Input is a number and calc not reset -> Update display & dispVal to reflect input
            if (!isDecimal) {
                dispVal = dispVal*10 + num;
                document.querySelector("#display").innerText += num;
            }
            else if (decimalFactor >= 0.001) {
                dispVal += num*decimalFactor;
                decimalFactor /= 10;
                document.querySelector("#display").innerText += num;
            }
            else {
                alert("Calculator cannot calculate more than 3 decimal places");
            }
        }
    }
    if (num==".")
        lastInput = 0;
    else
        lastInput = 1;
    if (dispVal > 999999999 || (decimalFactor == 0.01 && dispVal > 99999999.9) || 
    (decimalFactor == 0.001 && dispVal > 9999999.99) || (decimalFactor == 0.0001 && dispVal > 999999.999)) {
        clrNextPress = true;
        return document.querySelector("#display").innerText = "ERROR";
    }
}

function setOp(operator) {
    if (clearNextPress)
        return clr();
    console.log("Stored: " + storageVal + " Display: " + dispVal + " Operation: " + operator);
    if (!unresolvedOp) {
        console.log("no unresolved ops");
        storageVal = dispVal;
        pendingOp = operator;
        if (isReset) {
            isReset = false;
            unresolvedOp = true;
        }
    } else if (lastInput == 0) {
        alert("Error (1). Cannot Operate Without a Previous Complete Numerical Input");
        clr();
        console.log("setOp lastInput=0 triggered");
    } else { // unresolvedOp = true;
        storageVal = calculateUnresolved();
        console.log("setOp unresolvedOp triggered");
        pendingOp = operator;
    }
    resetDecimal();
    resetDisplayVars();
    lastInput = 0;
}

function calculateUnresolved () {
    if (pendingOp="+")
        return storageVal+dispVal;
    else if (pendingOp="-")
        return storageVal-dispVal;
    else if (pendingOp="*")
        return storageVal*dispVal;
    else // pendingOp = /
        if (dispVal == 0) {
            console.log("infinity");
            clearNextPress = true;
            document.querySelector("#display").innerText = "UNDEFINED";
            return 0;
        } else
            return (Math.floor(storageVal/dispVal*1000))/1000;
}

function calculate() {
    if (clearNextPress)
        return clr();
    console.log("calculate");
    console.log("Stored: " + storageVal + " Display: " + dispVal + " Operation: " + pendingOp);
    unresolvedOp = false;
    var result = 0;
    if (lastInput == 0) {
        alert("Error (2). Cannot Calculate Without Two Complete Numerical Inputs");
        return clr();
    }
    else if (lastInput == 1) { // Last Input was a number (0-9)
        console.log("mathed");
        if (pendingOp=="+")
            result = storageVal+dispVal;
        else if (pendingOp=="-")
            result = storageVal-dispVal;
        else if (pendingOp=="*")
            result = storageVal*dispVal;
        else if (pendingOp=="/")
            if (dispVal == 0) {
                console.log("infinity");
                clearNextPress = true;
                return document.querySelector("#display").innerText = "UNDEFINED";
            } else
                result = (Math.floor(storageVal/dispVal*1000))/1000;
        else
            return clr();
        lastOp = [pendingOp, dispVal];
        pendingOp = "";
    }
    else { // lastInput == 2 (last input was "calculate()")
        console.log(lastOp[0] + " " + lastOp[1]);
        if (lastOp[0]=="+")
            result = storageVal+lastOp[1];
        else if (lastOp[0]=="-")
            result = storageVal-lastOp[1];
        else if (lastOp[0]=="*")
            result = storageVal*lastOp[1];
        else if (lastOp[0]=="/")
            if (lastOp[1] == 0) {
                console.log("infinity");
                clearNextPress = true;
                return document.querySelector("#display").innerText = "UNDEFINED";
            } else
                result = (Math.floor(storageVal/lastOp[1]*1000))/1000;
        else
            return clr();
    }
    if (result > 999999999 || (isDecimal && result > 99999999.9) || 
    (decimalFactor == 0.01 && result > 9999999.99) || (decimalFactor == 0.001 && result > 999999.999)) {
        document.querySelector("#display").innerText = "ERROR";
        clearNextPress = true;
    } else {
        dispVal = result;
        storageVal = result;
        document.querySelector("#display").innerText = result;
    }
    if (document.querySelector("#display").innerText.length > 10)
        document.querySelector("#display").innerText = document.querySelector("#display").innerText.substring(0, 10);
    resetDecimal();
    lastInput = 2;
}

function clr() {
    clearNextPress = false;
    isReset = true;
    resetDecimal();
    resetDisplayVars();
    storageValue = 0;
    lastInput = 0;
    pendingOp = "";
    lastOp = "";
    unresolvedOp = false;
    document.querySelector("#display").innerText = 0;
    lastOp = "";
}

function resetDecimal() {
    console.log("reset decimals");
    isDecimal = false;
    decimalFactor = 0.1;
}

function resetDisplayVars() {
    console.log("reset display vars");
    dispVal = 0;
    dispStr = "";
    isDisplayReset = true;
    needResetDisplay = true;
}
