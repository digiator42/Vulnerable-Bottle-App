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
        <h2>List</h2>
        <a href="/cmd">Command Injection</a>
        <a href="/xss">Cross-Site Scripting (XSS)</a>
        <a href="/sqli">SQL Injection</a>
        <a href="/file_read">Insecure File Access</a>
        <a href="/csrf">CSRF</a>
        <a href="/open_redirect">Open Redirect</a>
        <a href="/ssrf">Server-Side Request Forgery</a>
        <a href="/directory_traversal">Directory Traversal</a>
    </div>

    <!-- Main Content -->
    <div class="main-content">
        <div class="form-container">
            {{ !base }}
        </div>
    </div>
</body>

</html>