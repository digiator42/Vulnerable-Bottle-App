<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vulnerable App</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>

<body>
    <!-- Sidebar -->
    <div class="sidebar">
        <h2>Vulnerabilities</h2>
        <!-- ends with ** is done -->
        <a href="/cmd">Command Injection **</a>
        <a href="/xss">Cross-Site Scripting (XSS) **</a>
        <a href="/sqli">SQL Injection</a>
        <a href="/admin">Brute Force</a>
        <a href="/buffer">Buffer Overflow **</a>
        <a href="/file-upload">File Upload **</a>
        <!-- <a href="/file-read">Insecure File Access</a> -->
        <!-- <a href="/csrf">CSRF</a> -->
        <!-- <a href="/open-redirect">Open Redirect</a> -->
        <!-- <a href="/ssrf">Server-Side Request Forgery</a> -->
        <!-- <a href="/directory-traversal">Directory Traversal</a> -->
        <!-- <a href="/crypto">Crypto</a>
        <a href="/deserialization">Deserialization</a>
        <a href="/dos">DOS Simulation</a>
        <a href="/email-injection">Email Injection</a>
        <a href="/jwt">JWT</a>
        <a href="/lfi">Local File Injection</a>
        <a href="/rfi">Remote File Injection</a> -->
    </div>

    <!-- Main Content -->
    <div class="main-content">
        <div class="form-container">

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
        <div class="code-div" onclick="codeWindow()">
            <a type="button">code</a>
        </div>
        <div class="logs-div" onclick="logsWindow()">
            <a type="button">logs</a>
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
    pureVuln = chunks[chunks.length - 1];

    if (url.indexOf('trigger') !== -1) {
        vuln = url.substr(url.indexOf('trigger') + 8);
    }
    else {
        vuln = pureVuln;
    }

    function logsWindow() {
        window.open(`/api/logs?vuln=${pureVuln}`, "", "width=700,height=400");
    }
    function codeWindow() {
        window.open(`/api/level_code?vuln=${vuln}`, "", "width=700,height=400");
    }

    let titleTag = document.getElementsByTagName('title');

    if (titleTag) {
        let h1Text = document.querySelector('h1').innerText;
        titleTag[0].innerText += " - " + h1Text;
    }
</script>

</html>