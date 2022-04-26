function getcontent() {
    var obj = new XMLHttpRequest();
    obj.onreadystatechange = function() {
        //4 means finished, 200 means ok
        if (obj.readyState == 4 && obj.status == 200) {
            document.getElementById("LearnMore").innerHTML = obj.responseText;
        }
    };
    obj.open("GET", "user/Info.html", true);
    obj.send();
}