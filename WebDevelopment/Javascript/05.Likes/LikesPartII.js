var neilLikeText = document.querySelector("#neil-likes");
var jimLikeText = document.querySelector("#jim-likes");
var nicholeLikeText = document.querySelector("#nichole-likes");
var jimLikes = 0;
var neilLikes = 0;
var nicholeLikes = 0;

function addLikes(id) {
    var element = document.querySelector(id);
    if (element.id=="neil") {
        neilLikes++;
        if (neilLikes == 1)
            neilLikeText.innerHTML = neilLikes + " Like";
        else
            neilLikeText.innerHTML = neilLikes + " Likes";
    }
    else if (element.id=="jim") {
        jimLikes++;
        if (jimLikes == 1)
            jimLikeText.innerHTML = jimLikes + " Like";
        else
            jimLikeText.innerHTML = jimLikes + " Likes";
    }
    else {
        nicholeLikes++;
        if (nicholeLikes == 1)
            nicholeLikeText.innerHTML = nicholeLikes + " Like";
        else
            nicholeLikeText.innerHTML = nicholeLikes + " Likes";
    }
}