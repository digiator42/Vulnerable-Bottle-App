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
        <a href="/cmd">Command Injection</a>
        <a href="/xss">Cross-Site Scripting (XSS)</a>
        <a href="/sqli">SQL Injection</a>
        <a href="/admin">Admin Access</a>
        <a href="/file_read">Insecure File Access</a>
        <a href="/csrf">CSRF</a>
        <a href="/open_redirect">Open Redirect</a>
        <a href="/ssrf">Server-Side Request Forgery</a>
        <a href="/directory_traversal">Directory Traversal</a>
        <a href="/buffer">Buffer Overflow</a>
        <a href="/crypto">Crypto</a>
        <a href="/deserialization">Deserialization</a>
        <a href="/dos">DOS Simulation</a>
        <a href="/email">Email Injection</a>
        <a href="/jwt">JWT</a>
        <a href="/lfi">Local File Injection</a>
        <a href="/rfi">Remote File Injection</a>
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
    chunks[chunks.length - 1];
    
    function logsWindow() {
        window.open(`/api/logs?vuln=${chunks[chunks.length - 1]}`, "", "width=600,height=400");
    }
    function codeWindow() {
        window.open(`/api/level_code?vuln=${chunks[chunks.length - 1]}`, "", "width=600,height=400");
    }
</script>

</html>