<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vulnerable Bottle App</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>

<body>
    <!-- Sidebar -->
    <div class="sidebar">
        <h2>Vulnerabilities</h2>
        <a href="/cmd-injection">Command Injection</a>
        <a href="/xss">Cross-Site Scripting (XSS)</a>
        <a href="/sqli">SQL Injection</a>
        <a href="/brute-force">Brute Force</a>
        <a href="/file-upload">File Upload</a>
        <a href="/file-read">Insecure File Access</a>
        <a href="/csrf">CSRF</a>
        <a href="/ssrf">Server-Side Request Forgery</a>
        <a href="/open-redirect">Open Redirect</a>
        <a href="/buffer-overflow">Buffer Overflow</a>
        <a href="/crypto">Crypto</a>
        <a href="/deserialization">Deserialization</a>
        <a href="/jwt">JWT</a>
    </div>

    <!-- Main Content -->
    <div class="main-content">
        <div class="form-container">
            <h3></h3>

            {{ !base }}
            <div class="dropdown-container">
                <label for="dropdown">Level:</label>
                <select id="dropdown" class="styled-dropdown">
                    <option value="" disabled selected>Select Level</option>
                    <option value="?level=weak">Weak</option>
                    <option value="?level=medium">Medium</option>
                    <option value="?level=strong">Strong</option>
                </select>
            </div>

        </div>
    </div>
    <div>
        <div class="help-div" onclick="helpWindow()">
            <a type="button">Help</a>
        </div>
        <div class="code-div" onclick="codeWindow()">
            <a type="button">Code</a>
        </div>
        <div class="logs-div" onclick="logsWindow()">
            <a type="button">Logs</a>
        </div>
        <div class="logout-div">
            <a type="button" href="/logout">Logout</a>
        </div>
    </div>
</body>
<script src="/static/js/main.js" type="module"></script>
<script>
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

    for (cookie of cookies) {
        if (cookie.trim().startsWith('vbausername')) {
            username = cookie.split('=')[1];
        }
    }

    document.querySelector('h3').innerText = 'Logged in as ' + username;
</script>

</html>