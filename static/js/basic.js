url = window.location.href;
chunks = url.split('/');
func_name = chunks[chunks.length - 1];

if (chunks.length > 4) {
    vuln = chunks.slice(-2).join('/');
}
else {
    vuln = func_name;
}

function helpWindow() {
    window.open(`/api/help?vuln=${func_name}`, "", "width=900,height=700");
}
function logsWindow() {
    window.open(`/api/logs?vuln=${func_name}`, "", "width=700,height=400");
}
function codeWindow() {
    window.open(`/api/level_code?vuln=${vuln}`, "", "width=700,height=400");
}

// Set title
let titleTag = document.getElementsByTagName('title');

if (titleTag) {
    let h1Text = document.querySelector('h1').innerText;
    titleTag[0].innerText += " - " + h1Text;
}

// welcome message
let cookies = document.cookie.split(';');
let username = '';

for (let cookie of cookies) {
    if (cookie.trim().startsWith('vbausername')) {
        username = cookie.split('=')[1];
    }
}

document.querySelector('h3').innerText = 'Logged in as ' + username;

// drag and drop
let dragValue;
let isDragging = false;
let startX, startY;
let footerDivs = document.querySelectorAll('.footer div');

function move() {
    for (let div of footerDivs) {
        div.style.position = 'absolute';

        div.onmousedown = function (event) {
            dragValue = div;
            isDragging = false;
            startX = event.pageX;
            startY = event.pageY;
        };

        div.onclick = function (event) {
            if (isDragging) {
                // prevent the click event while dragging
                event.preventDefault();
                event.stopPropagation();
            } else {
                // normal onclick event
                if (div.className === "help-div") {
                    helpWindow();
                }
                else if (div.className === "code-div") {
                    codeWindow();
                }
                else if (div.className === "logs-div") {
                    logsWindow();
                }
            }
        };
    }
}

document.onmouseup = function () {
    if (dragValue) {
        dragValue = null;
        setTimeout(() => (isDragging = false), 0);
    }
};

document.onmousemove = function (event) {
    if (dragValue) {
        isDragging = true;
        let x = event.pageX;
        let y = event.pageY;
        dragValue.style.left = (x - 25) + 'px';
        dragValue.style.top = (y - 10) + 'px';
    }
};

move();
