// var todHi = document.querySelector('#tod-hi');
// var hiTemp = document.querySelector('.hi');
// var hiTemp = document.querySelector('#hi');
// var loTemp = document.querySelector('.lo');
var fTempRanges = [["75°", "65°"],["80°", "66°"], ["69°", "61°"], ["78°", "70°"]];
var cTempRanges = [["24°", "18°"],["27°", "19°"],["21°", "16°"],["26°", "21°"]];

function hideCookies(id) {
    var element = document.querySelector(id);
    element.remove();
}

function loadReport() {
    alert("Loading weather report...");
}

function chooseUnits(element) {
    if (element.value == 'Celcius') {
        // console.log(hiTemp);
        // console.log(convertToF(hiTemp.innerText));
        // hiTemp.innerHTML = convertToF(hiTemp.innerHTML);
        // hiTemp.innerText = convertToF(hiTemp);
        // console.log(document.getElementsByClassName('.hi'));
        document.querySelector('#tod-hi').innerText = "24°";
        document.querySelector('#tod-lo').innerText = "18°";
        document.querySelector('#tom-hi').innerText = "27°";
        document.querySelector('#tom-lo').innerText = "19°";
        document.querySelector('#fri-hi').innerText = "21°";
        document.querySelector('#fri-lo').innerText = "16°";
        document.querySelector('#sat-hi').innerText = "26°";
        document.querySelector('#sat-lo').innerText = "21°";
    }
    else {
        document.querySelector('#tod-hi').innerText = "75°";
        document.querySelector('#tod-lo').innerText = "65°";
        document.querySelector('#tom-hi').innerText = "80°";
        document.querySelector('#tom-lo').innerText = "66°";
        document.querySelector('#fri-hi').innerText = "69°";
        document.querySelector('#fri-lo').innerText = "61°";
        document.querySelector('#sat-hi').innerText = "78°";
        document.querySelector('#sat-lo').innerText = "70°";
    }
}

function convertToF(value) {
    return parseInt(value) + 10;
}

function convertToC(value) {
    return value - 10;
}