console.log("page loaded...");


var mainVid = document.getElementById("IMSA-vid");
var side1 = document.getElementById("porsche");
var side2 = document.getElementById("yasDrift");
var side3 = document.getElementById("DPi");
var side4 = document.getElementById("soccer");

function playVid(num) {
    if (num == 7)
        mainVid.play();
    else if (num == 1)
        side1.play();
    else if (num == 2)
        side2.play();
    else if (num == 3)
        side3.play();
    else if (num == 4)
        side4.play();
    else
        console.log("...");
}

function sideVid(num) {
    setTimeout(function(){stopVid(num)},1500)
}

function stopVid(num) {
    if (num == 1)
        side1.pause();
    else if (num == 2)
        side2.pause();
    else if (num == 3)
        side3.pause();
    else if (num == 4)
        side4.pause();
    else
        console.log("...");
}