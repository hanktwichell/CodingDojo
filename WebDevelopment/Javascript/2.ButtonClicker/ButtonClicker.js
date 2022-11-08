var likes1=0;
var likes2=0;
var dislikes1=0;
var dislikes2=0;
// var loggedIn = new Boolean(false);
var isLoggedIn = 0;

function clickEvent() {
    var loggedIn = document.querySelector(".login");
    if (isLoggedIn) {
        loggedIn.innerHTML = "Login";
        isLoggedIn = 0;
    } else {
        loggedIn.innerHTML = "Logout";
        isLoggedIn = 1;
    }
}

// function hideButton() {
//     document.getElementById(".add-def").style.display = "none";
//     console.log("Hidden!");
// }

function hideButton() { // FIX THIS FUNCTION
    document.getElementById("defn-btn").style.display="none";
}

function addLike(num) {
    var buttonLikes1 = document.querySelector("#likes-1");
    var buttonLikes2 = document.querySelector("#likes-2");
    if (num==1) {
        likes1++;
        if (likes1 == 1)
            buttonLikes1.innerHTML = likes1 + " Like";
        else
            buttonLikes1.innerHTML = likes1 + " Likes";
    } else {
        likes2++;
        if (likes2 == 1)
            buttonLikes2.innerHTML = likes2 + " Like";
        else
            buttonLikes2.innerHTML = likes2 + " Likes";
    }
    alert("Ninja (Definition " + num + ") was liked!");
}

function addDislike(num) {
    var buttonDislikes1 = document.querySelector("#dislikes-1");
    var buttonDislikes2 = document.querySelector("#dislikes-2");
    if (num==1) {
        dislikes1++;
        if (dislikes1 == 1)
            buttonDislikes1.innerHTML = dislikes1 + " Dislike";
        else
            buttonDislikes1.innerHTML = dislikes1 + " Dislikes";
    } else {
        dislikes2++;
        if (dislikes2 == 1)
            buttonDislikes2.innerHTML = dislikes2 + " Dislike";
        else
            buttonDislikes2.innerHTML = dislikes2 + " Dislikes";
    }
    alert("Ninja (Definition " + num + ") was disliked :(");
}