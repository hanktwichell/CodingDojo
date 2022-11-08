console.log("page loaded...");
var numConnections = document.querySelector("#num-cons").innerHTML;
var numRequests = document.querySelector("#num-reqs").innerHTML;
var connectionsText = document.querySelector("#num-cons");
var requestsText = document.querySelector("#num-reqs");

function editProfile() {
    var newName = prompt("Name: ");
    document.querySelector("#user-name").innerHTML = newName;
    // alert(numConnections);
    // alert(userName);
    // alert(numRequests);
}

function accept(element) {
    // var requests = document.querySelector("#num-reqs");
    numConnections++;
    numRequests--;
    requestsText.innerHTML=numRequests;
    if (numConnections < 500)
        connectionsText.innerHTML=numConnections;
    else
        connectionsText.innerHTML="500+";
    removeRequest(element);
}

function decline(element) {
    numRequests--;
    requestsText.innerHTML=numRequests;
    removeRequest(element);
}

function removeRequest(element) {
    element.parentElement.parentElement.remove();
}

