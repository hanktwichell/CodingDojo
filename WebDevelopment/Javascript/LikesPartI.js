var numLikes = 0;
function addLike() {
    var likes = document.querySelector("#num-likes");
    numLikes++;
    if (numLikes == 1)
        likes.innerHTML = numLikes + " Like";
    else
        likes.innerHTML = numLikes + " Likes";
}
