var elements = []; // Query For Speedo UB
var input = document.querySelector("input"); //

window.onload = function() {
    if (JSON.parse(localStorage.getItem("elements")) != null) {
        elements = JSON.parse(localStorage.getItem("elements"));
        noob();
    }
}

function noob() {
// coming soon
}
