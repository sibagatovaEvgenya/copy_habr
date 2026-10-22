function setIcon() {
    const iconValue = document.getElementsByClassName(
        'category-icon'
    )[0].value;
    const iconElem = document.getElementById("icon");

    iconElem.className = `fa ${iconValue}`;
}

function addIcon() {
    const iconInput = document.getElementsByClassName(
        'category-icon'
    )[0];
    const iconPElem = iconInput.parentNode.children[0];
    const iconElem = document.createElement("i");

    iconPElem.classList.add("flex");
    iconPElem.classList.add("flex-js-sb");

    iconInput.addEventListener("input", setIcon);

    iconElem.id = "icon";
    iconElem.className = "fa"

    if (iconInput.value) {
        iconElem.className = `fa ${iconInput.value}`;
    }

    iconPElem.appendChild(iconElem);
}

document.addEventListener(
    "DOMContentLoaded", addIcon
);