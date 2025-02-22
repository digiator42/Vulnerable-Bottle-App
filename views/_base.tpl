<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vulnerable Bottle App</title>
    <link rel="stylesheet" href="/static/css/style.css">
    <link rel="stylesheet" href="/static/css/pygments.css">
</head>

<body>
    <!-- Sidebar -->
    <div class="sidebar">
        <h2>Vulnerabilities</h2>
        <a href="/cmd-injection">Command Injection</a>
        <a href="/sqli">SQL Injection</a>
        <a href="/xss">Cross-Site Scripting (XSS)</a>
        <a href="/ssrf">Server-Side Request Forgery (SSRF)</a>
        <a href="/csrf">Cross-Site Request Forgery (CSRF)</a>
        <a href="/ssti">Server-Side Template Injection (SSTI)</a>
        <a href="/brute-force">Brute Force</a>
        <a href="/file-upload">File Upload</a>
        <a href="/file-read">Insecure File Access</a>
        <a href="/open-redirect">Open Redirect</a>
        <a href="/buffer-overflow">Buffer Overflow</a>
        <a href="/deserialization">Deserialization</a>
        <a href="/crypto">Crypto</a>
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
    <div class="footer">
        <div class="help-div">
            <a type="button">Help</a>
        </div>
        <div class="code-div">
            <a type="button">Code</a>
        </div>
        <div class="logs-div">
            <a type="button">Logs</a>
        </div>
        <div class="logout-div">
            <a type="button" href="/logout">Logout</a>
        </div>
    </div>
</body>
<script src="/static/js/main.js" type="module"></script>
<script src="/static/js/basic.js" type="text/javascript"></script>

</html>